"""Location routes for the web interface."""

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.py_weather_2.core import LocationService

router = APIRouter()
templates = Jinja2Templates(
    directory=str(Path(__file__).parent.parent / "templates")
)


@router.get("/", response_class=HTMLResponse)
async def get_current_location(request: Request):
    """Get current location based on IP."""
    location_service = LocationService()
    location = location_service.get_current_location()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return templates.TemplateResponse(
        "location.html",
        {"request": request, "location": location},
    )


@router.get("/{zipcode}")
async def get_location_by_zip(request: Request, zipcode: str):
    """Get location by ZIP code."""
    location_service = LocationService()
    location = location_service.get_location_by_zip(zipcode)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return templates.TemplateResponse(
        "location.html", {"request": request, "location": location}
    )


@router.get("/api/current")
async def api_current_location():
    """API endpoint for current location."""
    location_service = LocationService()
    location = location_service.get_current_location()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return location


@router.get("/api/{zipcode}")
async def api_location_by_zip(zipcode: str):
    """API endpoint for location by ZIP."""
    location_service = LocationService()
    location = location_service.get_location_by_zip(zipcode)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return location
