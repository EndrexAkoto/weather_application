# Weather Application

## Overview
This Weather Application is a simple yet powerful web app that provides real-time weather data for any city worldwide. The app utilizes the OpenWeatherMap API to fetch current weather conditions, a 7-day forecast, and dynamic images based on the weather status (e.g., sunny, rainy, cloudy). It also displays additional weather information like temperature, humidity, wind speed, and sunrise/sunset times.

---

## Features

- **Real-Time Weather Data**: Displays the current temperature, weather condition, humidity, wind speed, and more.
- **Dynamic Weather Icons**: Shows relevant icons/images depending on the weather condition (e.g., sunny, cloudy, etc.).
- **7-Day Forecast**: Provides a weekly forecast starting from Sunday to the current day.
- **Date Display**: Displays today's date dynamically.
- **Responsive Design**: The app is styled for a seamless user experience on various devices.

---

## Screenshot

![Weather App Screenshot](../assets/screenshot.png)

## Features
- Search for current weather and a 7-day forecast.
- Displays temperature, humidity, wind speed, sunrise, and sunset for each day.
- Beautiful UI with a dynamic weather-themed background.


## Technologies Used

1. **Frontend**:
   - HTML
   - CSS
   - Jinja2 (for templating)

2. **Backend**:
   - Flask (Python web framework)
   - Python-dotenv (to manage environment variables)

3. **API**:
   - OpenWeatherMap API (for weather data)

---

## Setup Instructions

### Prerequisites

- Python 3.10 or higher installed on your system.
- An OpenWeatherMap API key (Sign up at [OpenWeatherMap](https://openweathermap.org/) to get one).

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd weather_application
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```plaintext
   API_KEY=your_openweathermap_api_key
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to use the app.

---

## File Structure

```
weather_application/
|
|-- app.py            # Flask application
|-- templates/
|   |-- index.html    # Main HTML template
|
|-- static/
|   |-- styles.css    # CSS for styling
|   |-- images/       # Images for weather icons
|
|-- requirements.txt  # Project dependencies
|-- .env              # Environment variables (not tracked in Git)
|-- .gitignore        # Files and directories to exclude from Git
```

---

## Usage

1. Open the application in your browser.
2. Enter the name of a city in the input field and click the "Search" button.
3. View the current weather information and the 7-day forecast dynamically displayed on the page.

---

## Future Enhancements

- Add hourly weather data.
- Implement geolocation for automatic city detection.
- Add support for multiple languages.
- Enhance the UI/UX with additional animations and themes.

---

## License

This project is licensed under the MIT License.

---

## Contributors

- **Endrex Martin Akoto**: Developer & Designer

