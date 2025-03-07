import requests
import pandas as pd
from datetime import datetime, timezone

# ✅ Corrected Open-Meteo API URL
API_URL = "https://api.open-meteo.com/v1/forecast"

# ✅ Corrected parameters
params = {
    "latitude": 53.5,  # Alberta Latitude
    "longitude": -114.0,  # Alberta Longitude
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m", \
    "timezone": "America/Edmonton"
}

# 🔍 Print full API request URL for debugging
full_url = f"{API_URL}?latitude={params['latitude']}&longitude={params['longitude']}&hourly={params['hourly']}&timezone={params['timezone']}"
print("🔍 API Request URL:", full_url)

# ✅ Fetch Data
response = requests.get(API_URL, params=params)

# ✅ save weather data
if response.status_code == 200:
    df = pd.DataFrame(response.json()["hourly"])
    df.to_csv("data/raw/weather_data.csv", index=False)
    with open("logs/fetch_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Weather data updated successfully.\n")
    print("✅ Weather data saved successfully!")
else:
    print("❌ API Request Failed!")
