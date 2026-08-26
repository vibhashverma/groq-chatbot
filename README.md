# ✨ Gemini AI Chatbot with Memory
A fast AI chatbot powered by **Google Gemini** using the Gemini 3.6 Flash model.
Built with Python (Flask) + Gemini API.

---

## ⚡ Quick Start (3 steps)

### Step 1 — Install dependencies
```cmd
pip install flask google-genai
```

### Step 2 — Set your Gemini API key and model
```cmd
set GEMINI_API_KEY=your_gemini_key_here
set GEMINI_MODEL=gemini-3.6-flash
```
> 🔑 Get your key at: https://aistudio.google.com/apikey
> Sign in with your Google account → Create API Key (takes 1 minute)

You can also put these in a `.env` file:
```dotenv
GEMINI_API_KEY=your_gemini_key_here
GEMINI_MODEL=gemini-3.6-flash
```

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
| ⚡ Fast | Powered by Gemini 3.6 Flash |
| 🧠 Memory | Remembers full conversation history |
| 📊 Speed meter | Live turns-remembered display |
| 🗑️ Clear memory | Reset and start fresh anytime |

---

## 📁 Project Structure

```
gemini-chatbot/
├── app.py              ← Flask backend
├── requirements.txt    ← Dependencies
├── README.md           ← This file
└── templates/
    └── index.html      ← Chat UI
```

---

## 🤖 Model Used
**gemini-3.6-flash** — Google's Gemini model, configurable via the `GEMINI_MODEL` environment variable.

---
