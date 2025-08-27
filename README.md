# Weather Data Fetcher

A Python script to fetch weather data securely without exposing API keys in the code.

## Setup

1. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variable**:
   - On Windows (Command Prompt):
     ```cmd
     set WEATHER_API_KEY=your_api_key_here
     ```
   - On Windows (PowerShell):
     ```powershell
     $env:WEATHER_API_KEY="your_api_key_here"
     ```
   - On Linux/Mac:
     ```bash
     export WEATHER_API_KEY=your_api_key_here
     ```

3. **Run the script**:
   ```bash
   python fetch_weather.py
   ```

## How It Works

- The API key is stored in an environment variable (`WEATHER_API_KEY`)
- The `config.py` file reads the API key from the environment variable using `python-dotenv`
- The `fetch_weather.py` script uses the API key from `config.py` to make requests to the OpenWeatherMap API
- Temperature is returned in Kelvin (default OpenWeatherMap unit)

## Security Features

- ✅ API keys are never hardcoded in source code
- ✅ Uses environment variables for secure storage
- ✅ Supports `.env` files for development (automatically loaded)
- ✅ Validates API key presence before making requests

## Example Usage

```bash
# Set the API key
set WEATHER_API_KEY=your_actual_api_key

# Run the script
python fetch_weather.py

# Enter city name when prompted
Enter the city name: London

# Example output:
# {'city': 'London', 'temperature': 290.45, 'weather': 'broken clouds'}
```

## Temperature Notes

- Temperature is returned in Kelvin by default
- To convert to Celsius: `celsius = kelvin - 273.15`
- To convert to Fahrenheit: `fahrenheit = (kelvin - 273.15) * 9/5 + 32`
