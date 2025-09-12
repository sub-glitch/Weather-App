#  Weather Forecast App

A simple **Streamlit-powered Weather Forecast App** that fetches real-time weather data from [OpenWeatherMap](https://openweathermap.org/) and displays it in an interactive dashboard with charts and visuals.

---

##  Features
- Get weather forecasts for **up to 7 days** 🌤️  
- Supports both **Temperature** and **Sky Conditions** views  
- 📊 Interactive charts using **Plotly**  
- 🗺 Google Maps integration to display the selected location  
- Smart **Sky Messages** and icons for better visualization  
- Automatic location detection via IP  

---



## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/weather-app.git
cd weather-app

2. **Create a virtual environment**
```bash 
python -m venv venv
source venv/bin/activate   # for Mac/Linux
venv\Scripts\activate      # for Windows

3.Install dependencies
```bash
pip install -r requirements.txt

4.Add your API key

5. Run the app

Tech Stack
Python
Streamlit
Plotly
Requests
OpenWeatherMapp API
Google Maps Embed

Project Structure
weather-app/
│── wf.py               # Main Streamlit app
│── backend.py           # Helper functions (API data fetching)
│── requirements.txt     # Project dependencies
images/              # App icons and visuals
│── README.md            # Project documentation

