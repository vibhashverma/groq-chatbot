from flask import Flask, request, jsonify, render_template, Response, stream_with_context
from groq import Groq
import json
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

    def generate():
        full_response = ""
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversations[session_id],
            max_tokens=1024,
            stream=True
        )
        for chunk in stream:
            token = chunk.choices[0].delta.content or ""
            if token:
                full_response += token
                yield f"data: {json.dumps({'token': token})}\n\n"

        conversations[session_id].append({
            "role": "assistant",
            "content": full_response
        })

        memory_count = len(conversations[session_id]) // 2
        yield f"data: {json.dumps({'done': True, 'memory_turns': memory_count})}\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")


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
        print("Run this first:  set GROQ_API_KEY=your_key_here\n")
    else:
        print("\n🤖 Groq AI Chatbot with Memory is running!")
        print("👉 Open http://localhost:5000 in your browser\n")
    app.run(debug=True, port=5000)
