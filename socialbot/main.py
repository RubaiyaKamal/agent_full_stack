import chainlit as cl
from agent import run_chatbot

# Import FastAPI app
from app import app as fastapi_app
from chainlit.server import app as chainlit_app

# Mount FastAPI under /api
chainlit_app.mount("/api", fastapi_app)

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    # Get chat history from session (or init)
    history = cl.user_session.get("chat_history", [])
    history.append({"role": "user", "content": user_input})

    # Run AI
    reply = await run_chatbot(user_input)
    history.append({"role": "assistant", "content": reply})

    # Save updated history
    cl.user_session.set("chat_history", history)

    await cl.Message(content=reply).send()
