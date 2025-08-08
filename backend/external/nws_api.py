import httpx
from datetime import date


async def get_weather_data(coords: dict[str, float], job_date: date):
    url = f"https://api.weather.gov/points/{coords['lat']},{coords['lon']}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        zone = data["properties"]["forecastZone"].split("/")[-1]
        alerts = await get_alerts(zone, client)
        forecasts = await get_forecast(data["properties"]["forecast"], job_date, client)
        weather_data = {"alerts": alerts, "forecasts": forecasts}
        return weather_data


async def get_alerts(zone: str, client: httpx.AsyncClient):
    url = f"https://api.weather.gov/alerts/active?zone={zone}"
    response = await client.get(url)
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


async def get_forecast(url: str, job_date: date, client: httpx.AsyncClient):
    response = await client.get(url)
    response.raise_for_status()
    data = response.json()
    periods = data["properties"]["periods"]
    forecasts = [
        period["detailedForecast"]
        for period in periods
        if job_date.strftime("%Y-%m-%d") in period["startTime"]
    ]
    return forecasts
