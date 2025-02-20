"""Web routes initialization."""

from .location import router as location_router
from .weather import router as weather_router

__all__ = ["location_router", "weather_router"]
