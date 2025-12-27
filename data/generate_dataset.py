import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

cities = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad',
          'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow']

states = {
    'Delhi': 'Delhi', 'Mumbai': 'Maharashtra', 'Kolkata': 'West Bengal',
    'Chennai': 'Tamil Nadu', 'Bangalore': 'Karnataka', 'Hyderabad': 'Telangana',
    'Ahmedabad': 'Gujarat', 'Pune': 'Maharashtra', 'Jaipur': 'Rajasthan',
    'Lucknow': 'Uttar Pradesh'
}

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

data = []

for city in cities:
    base_pm25 = np.random.uniform(50, 150)
    base_pm10 = base_pm25 * np.random.uniform(1.5, 2.0)
    base_no2 = np.random.uniform(30, 80)
    base_so2 = np.random.uniform(10, 30)
    base_co = np.random.uniform(0.5, 2.0)
    base_o3 = np.random.uniform(20, 60)

    for i, date in enumerate(date_range):
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * i / 365)
        weekend_factor = 0.8 if date.weekday() >= 5 else 1.0

        pm25 = max(0, base_pm25 * seasonal_factor * weekend_factor + np.random.normal(0, 20))
        pm10 = max(0, base_pm10 * seasonal_factor * weekend_factor + np.random.normal(0, 30))
        no2 = max(0, base_no2 * seasonal_factor * weekend_factor + np.random.normal(0, 10))
        so2 = max(0, base_so2 * seasonal_factor + np.random.normal(0, 5))
        co = max(0, base_co * seasonal_factor * weekend_factor + np.random.normal(0, 0.3))
        o3 = max(0, base_o3 * (2 - seasonal_factor) + np.random.normal(0, 8))

        aqi_values = [
            pm25 / 60 * 100,
            pm10 / 100 * 100,
            no2 / 80 * 100,
            so2 / 80 * 100,
            co / 2 * 100,
            o3 / 100 * 100
        ]
        aqi = max(aqi_values)

        if np.random.random() < 0.05:
            pm25 = np.nan
        if np.random.random() < 0.03:
            pm10 = np.nan

        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'City': city,
            'State': states[city],
            'PM2.5': round(pm25, 2),
            'PM10': round(pm10, 2),
            'NO2': round(no2, 2),
            'SO2': round(so2, 2),
            'CO': round(co, 2),
            'O3': round(o3, 2),
            'AQI': round(aqi, 2)
        })

df = pd.DataFrame(data)

df.to_csv('/tmp/cc-agent/61933487/project/data/air_quality_data.csv', index=False)
print(f"Dataset created successfully with {len(df)} records")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nDataset info:")
print(df.info())
