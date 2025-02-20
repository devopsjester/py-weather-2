"""Tests for location service."""

from unittest.mock import Mock, patch

import pytest

from py_weather_2.core.location_service import LocationService
from py_weather_2.core.models import Location


@pytest.fixture
def mock_location():
    return Location(
        city="San Francisco", state="CA", zip="94105", lat=37.7749, lon=-122.4194
    )


class TestLocationService:
    @patch("requests.get")
    def test_get_current_location_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "city": "San Francisco",
            "regionName": "California",
            "lat": 37.7749,
            "lon": -122.4194,
        }
        mock_get.return_value = mock_response

        # Test the method
        location = LocationService.get_current_location()

        assert location is not None
        assert location.city == "San Francisco"
        assert location.state == "CA"
        assert location.lat == 37.7749
        assert location.lon == -122.4194

    @patch("requests.get")
    def test_get_current_location_failure(self, mock_get):
        # Setup mock response for failure
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test the method
        location = LocationService.get_current_location()
        assert location is None

    @patch("requests.get")
    def test_get_location_by_zip_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "places": [
                {
                    "place name": "San Francisco",
                    "state": "California",
                    "latitude": "37.7749",
                    "longitude": "-122.4194",
                }
            ]
        }
        mock_get.return_value = mock_response

        # Test the method
        location = LocationService.get_location_by_zip("94105")

        assert location is not None
        assert location.city == "San Francisco"
        assert location.state == "CA"
        assert location.zip == "94105"
        assert location.lat == 37.7749
        assert location.lon == -122.4194

    @patch("requests.get")
    def test_get_location_by_zip_failure(self, mock_get):
        # Setup mock response for failure
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test the method
        location = LocationService.get_location_by_zip("00000")
        assert location is None
