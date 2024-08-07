import requests
import os
import json
import streamlit as st
from weather_emoji import weather_icons  # Assuming weather_icons is correctly imported

def save_location_data(city, country, lat, lon, file_path):
    location_data = {
        "city": city,
        "country": country,
        "latitude": lat,
        "longitude": lon
    }
    with open(file_path, 'w') as file:
        json.dump(location_data, file)

def load_location_data(file_path):
    with open(file_path, 'r') as file:
        location_data = json.load(file)
    return location_data

def get_coordinates(city, country, email):
    url = f"https://nominatim.openstreetmap.org/search?city={city}&country={country}&format=json"
    headers = {
        'User-Agent': f'MyWeatherApp/1.0 ({email})'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
            else:
                raise ValueError("City not found")
        except json.JSONDecodeError:
            raise ValueError("Error parsing JSON response")
    else:
        raise ValueError(f"Error fetching data from Nominatim API: {response.status_code}")

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error fetching data from Open-Meteo API: {response.status_code}")

def place_information():
    location_save_path = "saved_location.json"

    if os.path.exists(location_save_path):
        location_data = load_location_data(location_save_path)
        city = location_data['city']
        country = location_data['country']
        lat = location_data['latitude']
        lon = location_data['longitude']

        # Display loaded location data
        st.subheader("Initial Setup")
        st.write(f"City: {city}")
        st.write(f"Country: {country}")
        st.write(f"Latitude: {lat}")
        st.write(f"Longitude: {lon}")

    else:
        st.subheader("Initial Setup")
        email = st.text_input("Enter email (used for longitude and latitude API call): ")
        country = st.text_input("Enter country: ")
        city = st.text_input("Enter city: ")

        if st.button("Enter"):
            try:
                lat, lon = get_coordinates(city, country, email)
                save_location_data(city, country, lat, lon, location_save_path)
            except ValueError as e:
                st.error(f"Error: {e}")
                return None, None, None, None

    return city, country, lat, lon

def main():
    try:
        st.title("Weather App")
        city, country, lat, lon = place_information()

        if city and country and lat and lon:
            weather_data = get_weather(lat, lon)
            current_weather = weather_data.get('current_weather')

            if current_weather:
                st.subheader(f"Current weather in {city}, {country}:")
                st.write(f"Temperature: {current_weather['temperature']} °C")
                st.write(f"Wind Speed: {current_weather['windspeed']} km/h")
                st.write(f"Wind Direction: {current_weather['winddirection']}°")
                st.write(f"Weather Code: {weather_icons.get(current_weather['weathercode'], '❓')}")

            else:
                st.error("Weather data not available")

    except ValueError as e:
        print(f"error: {e}")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
