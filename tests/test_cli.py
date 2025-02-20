"""Tests for CLI commands."""
import pytest
from click.testing import CliRunner
from unittest.mock import patch
from weather import cli
from weather_app.models import Location, WeatherData

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def mock_location():
    return Location(
        city="San Francisco",
        state="CA",
        zip="94105",
        lat=37.7749,
        lon=-122.4194
    )

@pytest.fixture
def mock_weather():
    return WeatherData(
        temp_f=72.0,
        description="Sunny"
    )

class TestCliCommands:
    @patch('weather_app.location_service.LocationService.get_current_location')
    def test_where_is_current_location(self, mock_get_location, runner, mock_location):
        mock_get_location.return_value = mock_location
        result = runner.invoke(cli, ['where-is'])
        assert result.exit_code == 0
        assert "You are in San Francisco, CA" in result.output

    @patch('weather_app.location_service.LocationService.get_location_by_zip')
    def test_where_is_with_zipcode(self, mock_get_location, runner, mock_location):
        mock_get_location.return_value = mock_location
        result = runner.invoke(cli, ['where-is', '--zipcode', '94105'])
        assert result.exit_code == 0
        assert "94105 is in San Francisco, CA" in result.output

    @patch('weather_app.location_service.LocationService.get_current_location')
    def test_where_is_location_not_found(self, mock_get_location, runner):
        mock_get_location.return_value = None
        result = runner.invoke(cli, ['where-is'])
        assert result.exit_code == 0
        assert "Could not determine location" in result.output

    @patch('weather_app.location_service.LocationService.get_current_location')
    @patch('weather_app.weather_service.WeatherService.get_weather')
    def test_current_weather_current_location(self, mock_get_weather, mock_get_location, runner, mock_location, mock_weather):
        mock_get_location.return_value = mock_location
        mock_get_weather.return_value = mock_weather
        result = runner.invoke(cli, ['current'])
        assert result.exit_code == 0
        assert "It is currently 72.0ºF, and sunny in San Francisco, CA" in result.output

    @patch('weather_app.location_service.LocationService.get_location_by_zip')
    @patch('weather_app.weather_service.WeatherService.get_weather')
    def test_current_weather_with_zipcode(self, mock_get_weather, mock_get_location, runner, mock_location, mock_weather):
        mock_get_location.return_value = mock_location
        mock_get_weather.return_value = mock_weather
        result = runner.invoke(cli, ['current', '--zipcode', '94105'])
        assert result.exit_code == 0
        assert "It is currently 72.0ºF, and sunny in San Francisco, CA" in result.output

    @patch('weather_app.location_service.LocationService.get_current_location')
    def test_current_weather_location_not_found(self, mock_get_location, runner):
        mock_get_location.return_value = None
        result = runner.invoke(cli, ['current'])
        assert result.exit_code == 0
        assert "Could not determine location" in result.output

    @patch('weather_app.location_service.LocationService.get_current_location')
    @patch('weather_app.weather_service.WeatherService.get_weather')
    def test_current_weather_data_not_found(self, mock_get_weather, mock_get_location, runner, mock_location):
        mock_get_location.return_value = mock_location
        mock_get_weather.return_value = None
        result = runner.invoke(cli, ['current'])
        assert result.exit_code == 0
        assert "Could not retrieve weather data" in result.output