import os
from dotenv import load_dotenv

load_dotenv()

# Get the BASE_URL from environment variables
# Provide a default value if it's not set
BASE_URL = os.getenv("BASE_URL", "https://api.restful-api.dev/") # Default fallback
