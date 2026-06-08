from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(user_query):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_query
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"