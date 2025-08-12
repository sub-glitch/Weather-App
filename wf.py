import streamlit as sm
import plotly.express as pef
import requests
from backend import get_data

sky_messages = {
        "clear sky": "Clear skies ahead.",
        "few clouds": "A few clouds.",
        "scattered clouds": "Scattered clouds.",
        "broken clouds": "Partly cloudy 🌥 .",
        "overcast clouds": "Overcast ☁️.",
        "shower rain": "Showers expected 🌦.",
        "rain": "Rainy 🌧.",
        "light rain": "Light rain 🌦.",
        "thunderstorm": "Thunderstorms ⛈ – Stay indoors.",
        "snow": "Snowy ❄️ – Bundle up!",
        "mist": "Misty 🌫 – Low visibility ahead.",
    }

sky_images = {
    "clear sky": "images/clear.png",
    "few clouds": "images/cloud.png",
    "scattered clouds": "images/cloud.png",
    "broken clouds": "images/cloud.png",
    "overcast clouds": "images/cloud.png",
    "light rain": "images/rain.png",
    "moderate rain": "images/rain.png",
    "shower rain": "images/rain.png",
    "snow": "images/snow.png",
}

#sm.image("images/Covenant-University.png", width=200)
sm.title("Weather Forecast")

sm.markdown("""
    <style>
    .typing {
        width: 0;
        overflow: hidden;
        white-space: nowrap;
        border-right: 2px solid #ccc;
        font-size: 2em;
        font-weight: bold;
        color: gray;
        animation: typing 4s steps(40, end) forwards, blink 0.75s step-end infinite;
    }
    @keyframes typing {
        from { width: 0 }
        to { width: 25ch }
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }
    </style>
    <p class='typing'>In honour of Daniel Mordi🤍!</p>
""", unsafe_allow_html=True)

theme = sm.radio("Theme Mode:", ["Light", "Dark"])
if theme == "Dark":
    sm.markdown("""<style>
    body { background-color: #1e1e1e; color: white; }
    .smSlider > div > div > div > div { background-color: #555; }
    .smSelectbox > div > div { background-color: #555; color: white;}
    .smTextInput > div > div > input { background-color: #555; color: white;}
    </style>""", unsafe_allow_html=True)
else:
    sm.markdown("""<style>
    body { background-color: white; color: black; }
    .smSlider > div > div > div > div { background-color: #ddd; }
    .smSelectbox > div > div { background-color: #eee; color: black;}
    .smTextInput > div > div > input { background-color: #eee; color: black;}
    </style>""", unsafe_allow_html=True)

def get_location_by_ip():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return data.get("city", "")
    except requests.exceptions.RequestException:
        sm.warning("Could not determine location by IP. Please enter a city manually.")
        return ""

place = sm.text_input("Enter a location:", value=get_location_by_ip())  # Use value for initial input
days = sm.slider("Days: ", min_value=1, max_value=7, help="Select forecast days")
option = sm.selectbox("Select data to view",("Temperature", "Sky"))
sm.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filter_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
            figure = pef.line(x = dates, y= temperatures, labels={"x":"Date", "y":"Temperature(c)"})
            sm.plotly_chart(figure)

        elif option == "Sky":
            available_times = [entry["dt_txt"] for entry in filter_data]
            selected_time = sm.selectbox("Select a time of the day:", available_times, key="sky_time_selector")
            selected_entry = next((entry for entry in filter_data if entry["dt_txt"] == selected_time), None)

            if selected_entry:
                description = selected_entry["weather"][0]["description"]
                message = sky_messages.get(description, description.capitalize())
                image_path = sky_images.get(description, "images/cloud.png")
                if "rain" in description or "drizzle" in description:
                    sm.toast("☔️ Get an umbrella, it's going to rain!", icon="🌧")
                elif "storm" in description:
                    sm.toast("⛈ Thunderstorm alert! Stay safe.", icon="⚡️")
                elif "clear" in description:
                    sm.toast("☀️ Clear skies today – enjoy your day!", icon="😎")
                elif "clouds" in description :
                    sm.toast("☁️ Cloudy skies at the moment.", icon="☁️")
            sm.subheader(f"Sky forecast at {selected_time}")
            col1, col2 = sm.columns([1, 5])
            with col1:
                sm.image(image_path, width=60)
            with col2:
                sm.markdown(f"{message}")
        else:
            sm.warning("Forecast time not found.")
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=1&appid=c7af6baf7923374733758d0598666aed"
        geo_data = requests.get(geo_url).json()

        if geo_data:
            lat = geo_data[0]["lat"]
            lon = geo_data[0]["lon"]
            sm.subheader("📍 Google Map of Location")

            map_url = f"https://www.google.com/maps?q={lat},{lon}&hl=es;z=14&output=embed"
            sm.components.v1.iframe(map_url, width=700, height=450)
        else:
            sm.warning("Could not find location on map.")

    except Exception as e:
        sm.error(f"An error occurred: {e}")

    # --- Footer ---
    sm.markdown("""
        <hr style="margin-top: 50px;"/>
        <div style='text-align: center; color: gray; font-size: 0.9em;'>
            🌍 Weather Forecast App • Powered by OpenWeatherMap and Google Maps <br>
            © 2025 Developed by PYTHON TEAM — All rights reserved.
        </div>
        """, unsafe_allow_html=True)