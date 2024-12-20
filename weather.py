import requests
import os

city = input("Enter City: ")

# Fetch API key from environment variables
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    print("Error: API key not found. Set it in your environment variables.")
    exit()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print("\nWeather Information:")
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")
    else:
        print("City not found or other error occurred.")
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.json())
except Exception as e:
    print("An error occurred:", e)
