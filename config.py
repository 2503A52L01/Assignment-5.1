import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Fetch the API key from environment variables
API_KEY = os.getenv('WEATHER_API_KEY')

if not API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable is not set. Please set it in your environment or create a .env file.")
