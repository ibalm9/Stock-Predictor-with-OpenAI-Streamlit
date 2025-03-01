import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def analyze_stock(prompt):
    """
    Analyze stock data using OpenAI API
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Menggunakan model yang lebih terjangkau
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional stock market analyst. Analyze the given stock data and provide predictions."
                },
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        raise Exception(f"Error in OpenAI analysis: {str(e)}")