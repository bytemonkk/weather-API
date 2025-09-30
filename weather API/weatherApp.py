import requests  
API_KEY = "7d5ceac53fee2522ecab2aa2f801da69"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter city name: ")

url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    main = data['main']  
    temperature = main['temp']
    humidity = main['humidity']
    weather = data['weather'][0]['description']
    
    print(f"\nWeather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

else:
    print("Error:", response.status_code, response.text)
