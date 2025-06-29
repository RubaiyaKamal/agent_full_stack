---
title: ChatAssist AI
emoji: 🤖
colorFrom: indigo
colorTo: blue
sdk: docker
app_file: Dockerfile
pinned: false
---


# ChatAssist AI 🤖💬

Welcome to **ChatAssist AI**, a Chainlit-powered chatbot for WhatsApp/Messenger-style conversations.

## 🌟 Features
- ✅ OpenAI GPT-4 or Google Gemini
- ✅ Chat history using Chainlit session
- ✅ FastAPI backend (optional)
- ✅ Hugging Face Spaces ready

## 🛠 Setup (Local)

```bash
uv venv
source .venv/bin/activate
pip install -r requirements.txt
chainlit run main.py -w
