import requests

def print_first_five_paris_temperatures():
    # Your implementation goes here
    pass
    # Define the endpoint and parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.85,
        "longitude": 2.35,
        "hourly" : "temperature_2m"
    }

    # Make the GET request with the query parameters
    response = requests.get(url, params=params)

    res_json = response.json()
    hourly_json = res_json.get("hourly")
    temperature_2m_list = hourly_json.get("temperature_2m")
    value_count = 0
    for items in temperature_2m_list:
        print(items)
        value_count += 1
        if value_count == 5:
            break

print_first_five_paris_temperatures()
