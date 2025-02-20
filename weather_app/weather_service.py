"""Service for handling weather-related operations."""
import requests
from typing import Optional
from .models import WeatherData

class WeatherService:
    @staticmethod
    def get_weather(lat: float, lon: float) -> Optional[WeatherData]:
        """Get weather data from wttr.in"""
        response = requests.get(f'https://wttr.in/{lat},{lon}?format=j1')
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            return WeatherData(
                temp_f=float(current['temp_F']),
                description=current['weatherDesc'][0]['value']
            )
        return None