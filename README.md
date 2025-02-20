# py_weather_2

A Python application that provides both CLI and web interfaces for checking weather conditions using free, no-registration-required APIs.

## Features

- Get current weather conditions for your location
- Look up weather by ZIP code
- Show city and state for your current location
- Look up city and state by ZIP code
- Choose between CLI or web interface
- RESTful API endpoints for programmatic access

## Installation

1. Clone this repository
2. Install the package:
```bash
python3 -m pip install -e .
```

## Usage

### CLI Interface

Get weather for current location:
```bash
weather current
```

Get weather for a specific ZIP code:
```bash
weather current --zipcode 94105
```

Show your current location:
```bash
weather where-is
```

Show location for a ZIP code:
```bash
weather where-is --zipcode 94105
```

### Web Interface

Start the web server:
```bash
weather-web
```

Then open http://localhost:8000 in your browser.

### API Endpoints

- `GET /location/` - Get current location
- `GET /location/{zipcode}` - Get location by ZIP code
- `GET /location/api/current` - Get current location (JSON)
- `GET /location/api/{zipcode}` - Get location by ZIP (JSON)
- `GET /weather/` - Get current weather
- `GET /weather/{zipcode}` - Get weather by ZIP code
- `GET /weather/api/current` - Get current weather (JSON)
- `GET /weather/api/{zipcode}` - Get weather by ZIP (JSON)

## APIs Used

- IP Geolocation: ip-api.com
- ZIP Code Lookup: zippopotam.us
- Weather Data: wttr.in

## Development

### Setup Development Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
python3 -m pip install -r requirements.txt  # Install development dependencies
python3 -m pip install -e .  # Install in editable mode with src/ layout
```

### Project Structure
```
py-weather-2/
├── src/                    # Source code directory
│   ├── cli/               # Command-line interface
│   │   ├── __init__.py
│   │   └── main.py
│   ├── core/              # Shared business logic
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── constants.py
│   │   ├── location_service.py
│   │   └── weather_service.py
│   └── web/              # Web interface
│       ├── __init__.py
│       ├── app.py
│       ├── routes/
│       │   ├── location.py
│       │   └── weather.py
│       └── templates/
│           ├── base.html
│           ├── index.html
│           ├── location.html
│           └── weather.html
├── tests/               # Test directory
├── pyproject.toml      # Project configuration
├── requirements.txt    # Development dependencies
├── requirements.in     # Core dependencies
└── README.md
```

### Running Tests
```bash
pytest tests/
```

### Release Process
To create a new release:
1. Update version in `pyproject.toml`
2. Commit your changes
3. Tag the release:
```bash
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin v2.0.0
```

### Build from Source
To build the package locally:
```bash
python3 -m build
```

## License

MIT License