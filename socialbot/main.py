import chainlit as cl
from agent import run_chatbot
from storage import save_user_message, load_user_history

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hello! What's your name?").send()

@cl.on_message
async def on_message(message: cl.Message):
    if not cl.user_session.get("user_name"):
        user_name = message.content.strip()
        cl.user_session.set("user_name", user_name)
        await cl.Message(content=f"Nice to meet you, {user_name}! How can I help you today?").send()
        return

    user_name = cl.user_session.get("user_name")
    prompt = message.content

    reply = await run_chatbot(prompt)

    # Save history using user name
    save_user_message(user_name, prompt, reply)

    # Respond
    await cl.Message(content=reply).send()

@cl.on_action("history")
async def show_history():
    user_name = cl.user_session.get("user_name")
    history = load_user_history(user_name)

    if not history:
        await cl.Message(content="No chat history found.").send()
    else:
        formatted = "\n\n".join(
            f"🗨️ You: {entry['prompt']}\n🤖 Bot: {entry['response']}"
            for entry in history[-5:]
        )
        await cl.Message(content=formatted).send()
