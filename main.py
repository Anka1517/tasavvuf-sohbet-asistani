from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY", "").strip()
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").strip()

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)
