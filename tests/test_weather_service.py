"""Tests for weather service."""

from unittest.mock import Mock, patch

import requests

from py_weather_2.core.weather_service import WeatherService


class TestWeatherService:
    @patch("requests.get")
    def test_get_weather_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "current_condition": [{"temp_F": "72", "weatherDesc": [{"value": "Sunny"}]}]
        }
        mock_get.return_value = mock_response

        # Test the method
        weather = WeatherService.get_weather(37.7749, -122.4194)

        # Verify the correct URL was called
        mock_get.assert_called_once_with("https://wttr.in/37.7749,-122.4194?format=j1")

        # Verify the response parsing
        assert weather is not None
        assert weather.temp_f == 72.0
        assert weather.description == "Sunny"

    @patch("requests.get")
    def test_get_weather_http_error(self, mock_get):
        # Test various HTTP error codes
        for status_code in [400, 404, 500, 503]:
            mock_response = Mock()
            mock_response.status_code = status_code
            mock_get.return_value = mock_response

            weather = WeatherService.get_weather(0, 0)
            assert weather is None

    @patch("requests.get")
    def test_get_weather_malformed_response(self, mock_get):
        # Setup mock response with missing data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "current_condition": [{}]
        }  # Missing required fields
        mock_get.return_value = mock_response

        weather = WeatherService.get_weather(37.7749, -122.4194)
        assert weather is None

    @patch("requests.get")
    def test_get_weather_network_error(self, mock_get):
        # Test network connectivity issues
        mock_get.side_effect = requests.exceptions.RequestException()

        weather = WeatherService.get_weather(37.7749, -122.4194)
        assert weather is None
