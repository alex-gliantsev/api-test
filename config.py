import json
import os

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

try:
   with open(CONFIG_FILE_PATH, 'r') as f:
        _config_data = json.load(f)
except FileNotFoundError:
   print(f"Configuration file '{CONFIG_FILE_PATH}' not found. Using default values.")
   _config_data = {}

# Get values, providing defaults if not found or if file failed to load
BASE_URL = _config_data.get("BASE_URL", "https://api.restful-api.dev") # Default