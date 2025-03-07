import pandas as pd

df = pd.read_csv("data/raw/weather_data.csv")
df['timestamp'] = pd.to_datetime(df['time'])

df.rename(columns={"temperature_2m": "Temperature (°C)",
                   "relative_humidity_2m": "Humidity (%)",
                   "precipitation": "Precipitation (mm)",
                   "wind_speed_10m": "Wind Speed (km/h)"}, inplace=True)

df.to_csv("data/processed/cleaned_weather_data.csv", index=False)
print("Data cleaned and saved!")
