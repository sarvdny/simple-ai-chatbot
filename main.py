import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("./.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

def chat(message, _):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

demo = gr.ChatInterface(chat, title="Simple ChatBot by Sarvdny")
demo.launch()
