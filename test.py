from dotenv import load_dotenv
import os

load_dotenv()

def generate_response(user_query):
    return os.getenv("GOOGLE_API_KEY")