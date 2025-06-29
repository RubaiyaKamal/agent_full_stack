import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose provider: "openai" or "gemini"
PROVIDER = "gemini"  # or "openai"

async def run_chatbot(prompt: str) -> str:
    if PROVIDER == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]

    elif PROVIDER == "gemini":
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text

    else:
        return "Invalid provider selected!"
