import httpx
from datetime import date


async def get_weather_data(coords: dict[str, float], job_date: date) -> dict:
    url = f"https://api.weather.gov/points/{coords['lat']},{coords['lon']}"
    headers = {"User-Agent": "AutoJHA", "Accept": "application/geo+json"}
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url, timeout=15.0)
        response.raise_for_status()
        data = response.json()
        # Zone must be retrieved to access alerts for the area.
        zone = data["properties"]["forecastZone"].split("/")[-1]
        alerts = await get_alerts(zone, client)
        forecasts = await get_forecast(data["properties"]["forecast"], job_date, client)
        return {"alerts": alerts, "forecasts": forecasts}


async def get_alerts(zone: str, client: httpx.AsyncClient) -> list[dict]:
    url = f"https://api.weather.gov/alerts/active?zone={zone}"
    response = await client.get(url, timeout=15.0)
    response.raise_for_status()
    data = response.json()
    features = data["features"]
    alerts = []
    if features:
        alerts = [
            {
                "headline": feature["properties"]["headline"],
                "description": feature["properties"]["description"],
            }
            for feature in features
        ]
    return alerts


async def get_forecast(
    url: str, job_date: date, client: httpx.AsyncClient
) -> list[str]:
    response = await client.get(url, timeout=15.0)
    response.raise_for_status()
    periods = response.json()["properties"]["periods"]
    # Only retrieve forecasts for the date listed on the JHA.
    forecasts = [
        period["detailedForecast"]
        for period in periods
        if job_date.strftime("%Y-%m-%d") in period["startTime"]
    ]
    return forecasts
