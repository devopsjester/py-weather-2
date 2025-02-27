"""Weather routes."""

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from weather2.core import LocationService, WeatherService

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/", response_class=HTMLResponse)
async def get_current_weather(request: Request):
    """Get current weather for current location."""
    location_service = LocationService()
    location = location_service.get_current_location()

    if not location:
        return templates.TemplateResponse(
            "weather.html",
            {"request": request, "error": "Could not determine location"},
        )

    weather = WeatherService.get_weather(location.lat, location.lon)

    return templates.TemplateResponse(
        "weather.html",
        {
            "request": request,
            "weather": weather,
            "location": location,
        },
    )


@router.get("/{zipcode}", response_class=HTMLResponse)
async def get_weather_by_zip(request: Request, zipcode: str):
    """Get current weather for given ZIP code."""
    location_service = LocationService()
    location = location_service.get_location_by_zip(zipcode)

    if not location:
        return templates.TemplateResponse(
            "weather.html",
            {"request": request, "error": "Could not determine location"},
        )

    weather = WeatherService.get_weather(location.lat, location.lon)

    return templates.TemplateResponse(
        "weather.html",
        {
            "request": request,
            "weather": weather,
            "location": location,
        },
    )


@router.get("/api/current")
async def api_current_weather():
    """API endpoint for current weather."""
    location_service = LocationService()
    weather_service = WeatherService()

    location = location_service.get_current_location()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    weather = weather_service.get_weather(location.lat, location.lon)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return {"location": location, "weather": weather}


@router.get("/api/{zipcode}")
async def api_weather_by_zip(zipcode: str):
    """API endpoint for weather by ZIP."""
    location_service = LocationService()
    weather_service = WeatherService()

    location = location_service.get_location_by_zip(zipcode)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    weather = weather_service.get_weather(location.lat, location.lon)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return {"location": location, "weather": weather}
