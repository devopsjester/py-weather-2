"""Tests for weather service."""
import pytest
from unittest.mock import patch, Mock
from weather_app.weather_service import WeatherService
from weather_app.models import WeatherData

class TestWeatherService:
    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current_condition': [{
                'temp_F': '72',
                'weatherDesc': [{'value': 'Sunny'}]
            }]
        }
        mock_get.return_value = mock_response

        # Test the method
        weather = WeatherService.get_weather(37.7749, -122.4194)
        
        assert weather is not None
        assert weather.temp_f == 72.0
        assert weather.description == 'Sunny'

    @patch('requests.get')
    def test_get_weather_failure(self, mock_get):
        # Setup mock response for failure
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test the method
        weather = WeatherService.get_weather(0, 0)
        assert weather is None