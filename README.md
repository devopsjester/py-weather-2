# Weather CLI

A simple command-line weather application that shows current weather conditions for your location or a specified ZIP code. The application uses free, no-registration-required APIs for all functionality.

## Features

- Get current weather conditions for your location
- Look up weather by ZIP code
- Show city and state for your current location
- Look up city and state by ZIP code

## Installation

1. Clone this repository
2. Install the package:
```bash
pip install -e .
```

## Usage

### Get weather for current location
```bash
weather current
```

### Get weather for a specific ZIP code
```bash
weather current --zipcode 94105
```

### Show your current location
```bash
weather where-is
```

### Show location for a ZIP code
```bash
weather where-is --zipcode 94105
```

## APIs Used

- IP Geolocation: ip-api.com
- ZIP Code Lookup: zippopotam.us
- Weather Data: wttr.in

## Development

### GitHub Codespaces
This repository is configured for GitHub Codespaces. To get started:
1. Click the "Code" button on GitHub
2. Select "Create codespace on main"
3. Wait for the environment to build - all dependencies will be automatically installed
4. Start developing! The environment includes:
   - Python 3.12
   - Key VS Code extensions for Python development
   - Automatic code formatting with Black
   - Type checking and linting support

### Local Development
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests
```bash
pytest tests/
```

### Release Process
To create a new release:
1. Update version in `setup.py`
2. Commit your changes
3. Tag the release:
```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```
The GitHub Actions workflow will automatically:
- Run all tests
- Build the package
- Create a GitHub Release
- Attach build artifacts to the release

### Build from Source
To build the package locally:
```bash
python -m build
```
This will create distribution files in the `dist/` directory.

## License

MIT License