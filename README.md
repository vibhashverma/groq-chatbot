# ⚡ Groq AI Chatbot with Memory
A blazing-fast AI chatbot powered by **Groq** (FREE) using Llama 3.3 70B model.
Built with Python (Flask) + Groq API + real-time streaming.

---

## ⚡ Quick Start (3 steps)

### Step 1 — Install dependencies
```cmd
pip install flask groq
```

### Step 2 — Set your FREE Groq API key
```cmd
set GROQ_API_KEY=your_groq_key_here
```
> 🔑 Get your FREE key at: https://console.groq.com
> Sign up → API Keys → Create API Key (takes 1 minute)

### Step 3 — Run the app
```cmd
python app.py
```

Open your browser at:
```
http://localhost:5000
```

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ Ultra Fast | Groq LPU delivers 500+ tokens/sec |
| 🧠 Memory | Remembers full conversation history |
| 📡 Streaming | Real-time token-by-token responses |
| 🆓 100% Free | Groq free tier — no credit card needed |
| 📊 Speed meter | Live tokens/sec display |
| 🗑️ Clear memory | Reset and start fresh anytime |

---

## 📁 Project Structure

```
groq-chatbot/
├── app.py              ← Flask backend
├── requirements.txt    ← Dependencies
├── README.md           ← This file
└── templates/
    └── index.html      ← Chat UI
```

---

## 🤖 Model Used
**llama-3.3-70b-versatile** — Meta's powerful 70B model running on Groq's LPU hardware.
Free tier allows: 6,000 requests/day · 500,000 tokens/day
