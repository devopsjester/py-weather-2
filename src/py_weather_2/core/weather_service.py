"""Weather service functionality."""

from typing import Optional

import requests

from .models import WeatherData


class WeatherService:
    @staticmethod
    def get_weather(lat: float, lon: float) -> Optional[WeatherData]:
        """Get weather data from wttr.in"""
        try:
            url = f"https://wttr.in/{lat},{lon}?format=j1"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                current = data.get("current_condition", [{}])[0]

                try:
                    temp_f = current.get("temp_F")
                    weather_desc = current.get("weatherDesc", [{}])[0].get("value")

                    if temp_f is not None and weather_desc:
                        return WeatherData(
                            temp_f=float(temp_f), description=weather_desc
                        )
                except (KeyError, ValueError, TypeError, IndexError):
                    return None
            return None
        except requests.exceptions.RequestException:
            return None
