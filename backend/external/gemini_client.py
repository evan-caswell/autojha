from google import genai
from backend.core.config import get_settings
from backend.schemas.jha_schema import JHA


def get_gemini_response(prompt: str) -> JHA:
    client = genai.Client(api_key=get_settings().GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": JHA
        })
    return JHA.model_validate_json(response.text) # type: ignore
