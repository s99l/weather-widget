import streamlit as st
import requests
import os
from dotenv import load_dotenv
from streamlit_autorefresh import st_autorefresh
# load_dotenv()
try:
    API_KEY = st.secrets["API_KEY"]
except Exception:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")


st.set_page_config(page_title="Friends' Weather Board", page_icon="🌤", layout="centered")

st_autorefresh(interval=5 * 60 * 1000, key="auto-refresh")

st.markdown("""
    <div style='text-align: center; margin-top: -40px;'>
        <h1 style='font-size: 3em;'>🌍 Friends' Live Weather Board</h1>
        <p style='font-size: 1.2em; color: gray;'>From Mumbai to Jammu — stay synced with the skies ☁️</p>
        <p style='font-size: 0.9em; color: #999;'>Auto-refreshes every 5 minutes ⏱️</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    div.stButton > button:first-child {
        
        background-color: #f0f2f6;
        color: #555;
        padding: 10px 24px;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-size: 1em;
        transition: 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: black;
        color: red;
    }
    </style>
""", unsafe_allow_html=True)


# Create a "Get Weather" button
col1, col2, col3 = st.columns([1, 1, 1])
button_clicked = False

with col2:
    if st.button("🌦️ Get Weather Updates"):
        button_clicked = True

if button_clicked:
    cities = {
        "Navi Mumbai": "Ghansoli, IN",
        "Jammu": "Jammu, IN",
        "Gurgaon": "Gurgaon, IN"#,
        # "Singrauli": "Singrauli, IN"
    }

    weather_emojis = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️"
    }

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

    with st.spinner("Fetching latest weather..."):
        for name, city in cities.items():
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            st.markdown("###")

            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                weather_main = data["weather"][0]["main"]

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

else:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # 🌟 Centered-like message, full-width
        st.markdown("""
            <div style="
                background-color: #e7f3fe;
                border-left: 6px solid #2196F3;
                padding: 10px 16px;
                border-radius: 8px;
                margin-top: 20px;
                color: #333;
                font-size: 16px;
            ">
                <strong>💡 Tip:</strong> No Weather 😱? Click above to get it!
            </div>
        """, unsafe_allow_html=True)
