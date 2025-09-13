# Simple chatbot using python

Hello everyone, Sarvdny here!
I would like to say that this is my very first A.I chatbot by using openAI and Gradio
So let me quickly tell you how to run this chatbot:

## Setup:

1. Install uv from https://docs.astral.sh/uv/
2. Clone this repo to your device
3. Make a `.env` file inside the folder itelf
4. Add the given variables inside the `.env` file
```code
OPENAI_API_KEY="Your_API_Key"
OPENAI_MODEL="Your preferred AI model"
OPENAI_BASE_URL="API base URL"
```
5. After saving all, just type:
    ```bash
    uv init
    uv sync
    uv run main.py
    ```
    ---
    After a successfull connection your AI will be online!
    # thankyou :)

The chatbot will open in your browser at http://localhost:7860
