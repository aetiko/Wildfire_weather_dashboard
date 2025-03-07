import pandas as pd

#  Load cleaned weather data
df = pd.read_csv("data/processed/cleaned_weather_data.csv")

#  Convert time column to datetime
df["time"] = pd.to_datetime(df["time"])

#  Calculate Simplified Fire Weather Index (FWI)
df['FWI'] = (df['Temperature (°C)'] * 0.3) + (df['Wind Speed (km/h)'] * 0.2) - (df['Humidity (%)'] * 0.1) + (df['Precipitation (mm)'] * 0.05)

#  Save FWI results
df.to_csv("data/fwi_calculations/fwi_results.csv", index=False)

print(" Fire Weather Index (FWI) calculated and saved!")
