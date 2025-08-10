from google import genai
from backend.core.config import get_settings


def get_gemini_response(prompt: str) -> str | None:
    client = genai.Client(api_key=get_settings().GEMINI_API_KEY)

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text
