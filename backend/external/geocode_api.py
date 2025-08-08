import httpx
from backend.core.config import get_settings


async def get_coords(location: str):
    url = "https://geocode.xyz"
    params = {
        "auth": get_settings().GEOCODE_API_KEY,
        "locate": location,
        "region": "US",
        "geoit": "JSON",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        coords = {
            "lat": round(float(data["latt"]), 4),
            "lon": round(float(data["longt"]), 4),
        }
        return coords
