from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
 
app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
 
# In-memory conversation store: { session_id: [messages] }
conversations = {}
 
SYSTEM_PROMPT = """You are a helpful, friendly, and intelligent AI assistant with memory.
You remember everything said in this conversation and refer back to it naturally.
Be concise but warm. When the user mentions something personal (name, interests, goals),
remember it and use it later to personalize your responses."""
 
 
@app.route("/")
def index():
    return render_template("index.html")
 
 
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    session_id = data.get("session_id", "default")
    user_message = data.get("message", "").strip()
 
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
 
    if session_id not in conversations:
        conversations[session_id] = []
 
    conversations[session_id].append({
        "role": "user",
        "content": user_message
    })
 
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversations[session_id],
        max_tokens=1024
    )
 
    reply = response.choices[0].message.content
 
    conversations[session_id].append({
        "role": "assistant",
        "content": reply
    })
 
    memory_count = len(conversations[session_id]) // 2
    return jsonify({
        "token": reply,
        "done": True,
        "memory_turns": memory_count
    })
 
 
@app.route("/api/clear", methods=["POST"])
def clear():
    data = request.json
    session_id = data.get("session_id", "default")
    conversations.pop(session_id, None)
    return jsonify({"status": "cleared"})
 
 
@app.route("/api/memory", methods=["GET"])
def memory():
    session_id = request.args.get("session_id", "default")
    history = conversations.get(session_id, [])
    return jsonify({
        "turns": len(history) // 2,
        "messages": history
    })
 
 
if __name__ == "__main__":
    if not os.environ.get("GROQ_API_KEY"):
        print("\n❌ ERROR: GROQ_API_KEY not set!")
        print("Run this first: set GROQ_API_KEY=your_key_here\n")
    else:
        print("\n🤖 Groq AI Chatbot with Memory is running!")
        print("👉 Open http://localhost:5000 in your browser\n")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
