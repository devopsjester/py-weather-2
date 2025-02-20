"""CLI interface module."""

import click

from weather2.core.location_service import LocationService
from weather2.core.weather_service import WeatherService


@click.group()
def cli():
    """Weather CLI application"""
    pass


@cli.command()
@click.option("--zipcode", help="ZIP code to look up")
def where_is(zipcode):
    """Show the city and state for a location"""
    location_service = LocationService()
    location = (
        location_service.get_location_by_zip(zipcode)
        if zipcode
        else location_service.get_current_location()
    )

    if location:
        if zipcode:
            click.echo(f"{location.zip} is in {location.city}, {location.state}")
        else:
            click.echo(f"You are in {location.city}, {location.state}")
    else:
        click.echo("Could not determine location")


@cli.command()
@click.option("--zipcode", help="ZIP code to look up weather for")
def current(zipcode):
    """Show current weather conditions"""
    location_service = LocationService()
    weather_service = WeatherService()

    location = (
        location_service.get_location_by_zip(zipcode)
        if zipcode
        else location_service.get_current_location()
    )

    if not location:
        click.echo("Could not determine location")
        return

    weather = weather_service.get_weather(location.lat, location.lon)
    if weather:
        msg = (
            f"It is currently {weather.temp_f}ºF, "
            f"and {weather.description.lower()} in {location.city}, {location.state}"
        )
        click.echo(msg)
    else:
        click.echo("Could not retrieve weather data")
