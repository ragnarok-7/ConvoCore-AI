import os
from dotenv import load_dotenv

env_path = r"C:\Users\KIIT\OneDrive\Documents\Projects\panchal ai agent\.env"

load_dotenv(env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")