import requests
from langchain.agents import tool

@tool
def get_weather(location):
    """Returns the weather and temperature of a specific location asked"""
    api_key='sk-proj-mD04a3mBhMHVoxLxF7mmT3BlbkFJ98XR86inj890MqOftFeL'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather: {weather}, Temperature: {temperature}K"
    else:
        return "Could not get weather data."
