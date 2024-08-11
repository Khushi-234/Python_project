import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if not weather_data:
        return

    current_weather = weather_data['list'][0]
    max_temp_of_day = max(entry['main']['temp'] for entry in weather_data['list'])

    print('\n----------------------------------')
    print("\tCurrent Weather")
    print('----------------------------------')

    print(f"City: {weather_data['city']['name']}")
    print(f"Current Temperature: {current_weather['main']['temp']}°C")
    print(f"Maximum Estimated Temperature of the Day: {max_temp_of_day}°C")
    print(f"Humidity: {current_weather['main']['humidity']}%")
    print(f"Weather: {current_weather['weather'][0]['description']}")

def main():
    api_key = ""  
    location = input("Enter city or ZIP code: ")

    if not location:
        print("Please enter a valid location.")
        return

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
