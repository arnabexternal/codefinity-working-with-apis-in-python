import requests

def fetch_berlin_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    temperature = data["current_weather"]["temperature"]  # Replace with the actual temperature value from data
    windspeed = data["current_weather"]["windspeed"]    # Replace with the actual wind speed value from data
    print(f"Temperature: {temperature}°C, Wind Speed: {windspeed} m/s")

fetch_berlin_weather()
