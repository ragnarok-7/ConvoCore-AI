from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def ask_llm(prompt):

    try:

        completion = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        if completion.choices:

            return completion.choices[0].message.content

        else:

            return "Sorry, I couldn't generate a response."

    except Exception as e:

        return f"Error: {str(e)}"