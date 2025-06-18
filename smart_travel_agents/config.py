from dotenv import load_dotenv
import os
# loads API keys and project configuration values from a .env file 
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET = os.getenv("DATASET")
TABLE = os.getenv("TABLE")
