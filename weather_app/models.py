"""Data models for the weather application."""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Location:
    city: str
    state: str
    zip: str
    lat: float
    lon: float

@dataclass
class WeatherData:
    temp_f: float
    description: str