# Demo prompts for building this app

## Instructions
Use Copilot in Agent mode (I used Claude 3.5 Sonnet as the model) and run these prompts. Results may vary, but here are the prompts I used:

## Prompts

Agentic Weather in Python

```
Create a new CLI weather app. The app will be in Python using Click CLI. The app will be called weather. Add a file called “.github/copilot-instructions.md” that says “Only use free APIs. Prefer APIs that do not require registration or any kind of token or username.”

The first command, “where-is” will show the city and state. If a zip code is provided with the “--zipcode” switch, base off that, otherwise use current location. Output should be like “<zipcode> is in <city>, <state>.”

The second command, “current" will show the current temperature (in imperial units) and weather conditions. if a "--zipcode" argument is provided it will show the conditions for that zipcode, otherwise use current location. Output should be like “It is currently <temperature>ºF, and <weather condition> in <city>, <state>.”
```

```
run the where-is command
```

```
make the weather conditions lower case, and use the state abbreviation instead of the full name.
```

```
run all commands
```

```
restructure this project according to SOLID principles.
```

```
add unit tests for both commands
```

```
fix failing test
```

```
Add a gitignore file
```

```
Add a setup script and readme file
```

```
Add a codespace configuration
```

```
Add a GitHub Actions CI build
```

```
Ensure that the project name is a valid PEP 508 identifier (only alphanumeric characters, underscores, and hyphens are allowed, and it must start with a letter or underscore).
```

```
run the build command to verify that the TOML file creates a package correctly
```

```
Create release 2.0.0
```

### Notes
This might be needed, depending on how Copilot configures virtual environments
```
instead of "pip install", you need to run "python3 -m pip install"
```