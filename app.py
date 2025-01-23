from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Initialize the Flask app
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    forecast_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            # Fetch current weather data
            current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(current_weather_url)
            if response.status_code == 200:
                weather_data = response.json()

                # Format sunrise and sunset times
                sunrise = datetime.utcfromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M:%S')
                sunset = datetime.utcfromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M:%S')
                weather_data['sys']['sunrise_formatted'] = sunrise
                weather_data['sys']['sunset_formatted'] = sunset

                # Fetch weekly forecast data
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                forecast_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric"
                forecast_response = requests.get(forecast_url)
                if forecast_response.status_code == 200:
                    forecast_data = forecast_response.json()

                    # Reorder forecast to start from Sunday
                    today_index = datetime.today().weekday()  # Monday=0, Sunday=6
                    forecast_data['daily'] = forecast_data['daily'][7 - today_index:] + forecast_data['daily'][:7 - today_index]
            else:
                error = "City not found. Please try again."
        else:
            error = "Please enter a city name."

    # Get today's date
    today_date = datetime.now().strftime('%A, %d %B %Y')

    return render_template("index.html", weather_data=weather_data, forecast_data=forecast_data, error=error, today_date=today_date)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
