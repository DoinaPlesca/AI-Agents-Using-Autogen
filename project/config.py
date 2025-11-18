
##########Autogen Configuration
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": MISTRAL_API_KEY,
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "repeat_penalty": 1.1,
            "temperature": 0.0,
            "seed": 42,
            "stream": False,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}

