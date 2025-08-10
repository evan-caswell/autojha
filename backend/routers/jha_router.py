from fastapi.routing import APIRouter
from backend.schemas.jha_schema import JobData
from backend.utils.prompt_templates import jha_prompt
from backend.external.gemini_client import get_gemini_response
from backend.external.geocode_api import get_coords
from backend.external.nws_api import get_weather_data

router = APIRouter(prefix="/jha")


@router.post("/generate")
async def generate_jha(input_data: JobData):
    # Lat and lon need to be retrieved using the city and state to access the NWS API.
    coords = await get_coords(input_data.job_location)
    weather_data = await get_weather_data(coords, input_data.job_date)
    prompt = jha_prompt(input_data, weather_data)
    response = get_gemini_response(prompt)
    return response
