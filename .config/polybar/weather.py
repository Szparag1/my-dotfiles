#!/usr/bin/env python3

import requests
import sys

# OpenWeatherMap API configuration
API_KEY = "xxx"  # Replace with your OpenWeatherMap API key
CITY = "xxx"  # Replace with your city or use City ID
UNITS = "metric"  # Options: 'metric', 'imperial', 'standard'
LANG = "pl"  # Language for weather description
lat = "xxx"
lon = "xxx"

# Font Awesome icons mapping
ICONS = {
    "01d": "",  # clear sky (day)
    "01n": "",  # clear sky (night)
    "02d": "",  # few clouds (day)
    "02n": "",  # few clouds (night)
    "03d": "",  # scattered clouds
    "03n": "",  # scattered clouds
    "04d": "",  # broken clouds
    "04n": "",  # broken clouds
    "09d": "",  # shower rain
    "09n": "",  # shower rain
    "10d": "",  # rain (day)
    "10n": "",  # rain (night)
    "11d": "",  # thunderstorm
    "11n": "",  # thunderstorm
    "13d": "",  # snow
    "13n": "",  # snow
    "50d": "",  # mist
    "50n": "",  # mist
}

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={UNITS}&lang{LANG}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant data
        temp = weather_data["main"]["temp"]
        icon_code = weather_data["weather"][0]["icon"]
        description = weather_data["weather"][0]["description"]

        # Get the corresponding icon
        icon = ICONS.get(icon_code, "?")

        # Format the output
        return f"{icon} {temp:.1f}°C"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_weather())
