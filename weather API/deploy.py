import requests
import streamlit as st

st.title("Weather App")

city = st.text_input("Enter city name:")

API_KEY = "7d5ceac53fee2522ecab2aa2f801da69"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

if city:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']

        st.subheader(f"Weather in {city}")
        st.write(f"Temperature: {main['temp']} °C")
        st.write(f"Humidity: {main['humidity']}%")
        st.write(f"Condition: {weather}")

    else:
        st.error("City not found or invalid API key!")
