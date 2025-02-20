"""Core data models."""
from dataclasses import dataclass

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