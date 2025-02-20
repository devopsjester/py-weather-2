"""Location service functionality."""

from typing import Optional

import requests

from .constants import STATE_ABBREV
from .models import Location


class LocationService:
    @staticmethod
    def get_current_location() -> Optional[Location]:
        """Get location data from IP address using ip-api.com"""
        response = requests.get("http://ip-api.com/json/")
        if response.status_code == 200:
            data = response.json()
            return Location(
                city=data["city"],
                state=STATE_ABBREV.get(data["regionName"], data["regionName"]),
                zip="",
                lat=float(data["lat"]),
                lon=float(data["lon"]),
            )
        return None

    @staticmethod
    def get_location_by_zip(zipcode: str) -> Optional[Location]:
        """Get location data from zipcode using zippopotam.us"""
        response = requests.get(f"https://api.zippopotam.us/us/{zipcode}")
        if response.status_code == 200:
            data = response.json()
            place = data["places"][0]
            return Location(
                city=place["place name"],
                state=STATE_ABBREV.get(place["state"], place["state"]),
                zip=zipcode,
                lat=float(place["latitude"]),
                lon=float(place["longitude"]),
            )
        return None
