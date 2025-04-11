import webview
import subprocess
import time

# Start Streamlit app in background
subprocess.Popen(["streamlit", "run", "weather_app.py"])

# Give it time to start
time.sleep(3)

# Open it in a native window
webview.create_window(
    "My Weather Widget",
    "http://localhost:8501",
    width=400,
    height=600,
    resizable=False,
    frameless=True  # Looks more like a widget
)

webview.start()
