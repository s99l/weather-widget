import streamlit as st
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
# pip install -r requirements.txt

# List of locations
cities = {
    "Navi Mumbai": "Ghansoli, IN",
    "Jammu": "Jammu, IN",
    "Gurgaon": "Gurgaon, IN",
    "Singrauli": "Singrauli, IN"
}

# Emoji mapper for weather conditions
weather_emojis = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️"
}

st.set_page_config(page_title="Friends' Weather Board", layout="centered")
st.title("🌍 Friends' Live Weather Board")

refresh_interval = 300  # in seconds (5 minutes)
st.caption("Auto-refreshes every 5 minutes ⏱️")
time.sleep(1)

for name, city in cities.items():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    st.markdown("###")

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_main = data["weather"][0]["main"]
        # Choose background color based on weather
        weather_colors = {
            "Clear": "#FFD700",
            "Clouds": "#D3D3D3",
            "Rain": "#87CEFA",
            "Drizzle": "#ADD8E6",
            "Thunderstorm": "#8B0000",
            "Snow": "#E0FFFF",
            "Mist": "#C0C0C0",
            "Fog": "#C0C0C0"
        }
        bg_color = weather_colors.get(weather_main, "#F5F5F5")

        emoji = weather_emojis.get(weather_main, "🌡️")

        st.markdown(f"""
            <div style='
                background-color: {bg_color};
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                color: #222222;
            '>
                <h4 style='color: #333333;'>📍 {name}</h4>
                <p style='font-size: 24px; color: #111111;'>{emoji} <strong>{weather_main}</strong>, {temp}°C</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Could not fetch weather for {name}")


time.sleep(refresh_interval)
st.rerun()
