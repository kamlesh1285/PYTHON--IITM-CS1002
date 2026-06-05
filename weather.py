import os
import math 
from open_meteo import forecast

def get_weather():
    """Get current weather using FREE Open-Meteo API (No API key needed)"""
    lat = os.getenv("WEATHER_LAT", "28.6139")  # Default IIT Delhi
    lon = os.getenv("WEATHER_LON", "77.2090")
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weathercode&hourly=temperature_2m&timezone=Asia/Kolkata"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        # Convert WMO code to description
        conditions = {0: "Clear", 1: "Mainly clear", 3: "Overcast", 61: "Rain", 63: "Rain", 95: "Thunderstorm"}
        condition = conditions.get(data['current']['weathercode'], "Unknown")
        
        return {
            'temp': data['current']['temperature_2m'],
            'condition': condition,
            'humidity': data.get('current', {}).get('relative_humidity_2m', 'N/A'),
            'wind_speed': data['current'].get('wind_speed_10m', 'N/A')
        }
    except:
        return {'temp': 25, 'condition': 'Sunny', 'error': 'API unavailable'}