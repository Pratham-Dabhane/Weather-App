# importing libraries
import datetime as dt
import requests


# Setting base URLs and  API keys
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


# Taking the input of the city from the user
CITY = input(str("Enter the city: "))


# Function to convert the default kelvin temperature to celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)


# Throwing the error if anything goes wrong
try:

    
    # Creating the URL for the unique city
    url = f"{BASE_URL}appid={API_KEY}&q={CITY}"


    # Converting the response into JSON format
    response = requests.get(url).json()


    # Extracting and converting the data from the response
    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


    # Dynamically printing all the data from the response
    print(f"Temperature: {temp_celsius}\nFeels like: {feels_like_celsius}\nWind speed: {wind_speed}\nHumidity: {humidity}\nDescription: {description}\nSunrise: {sunrise_time}\nSunset: {sunset_time}")


# Dynamically returning the error message on any ERROR
except :
    print(f"Error: {response['message']}")