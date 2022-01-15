import requests, os
from twilio.rest import Client
from user import User
import apitokens

# figure out a way to store these keys as environment variables cause its not working rn

# openweather API information
APP_ID = apitokens.APP_ID

# Geocoding API information
GEOCODING_KEY = apitokens.GEOCODING_KEY

# twilio account information
ACCOUNT_SID = apitokens.ACCOUNT_SID
AUTH_TOKEN = apitokens.AUTH_TOKEN

class WeatherTexter:
    def __init__(self, user: User):
        self.user = user
        self.params = {
            'key': GEOCODING_KEY,
            'address': self.user.address
        }
        # API endpoint for Google Geolocation
        self.location_data = requests.get(url='https://maps.googleapis.com/maps/api/geocode/json?',
                                          params=self.params).json()
        # accessing the user's coordinates using their address so it can be fed into the weather application
        self.lat = self.location_data['results'][0]['geometry']['location']['lat']
        self.lng = self.location_data['results'][0]['geometry']['location']['lng']

        self.weather_apiparams = {
            'appid': APP_ID,
            'lon': self.lng,
            'lat': self.lat,
            'units': 'metric',
            'exclude': 'current,minutely,daily'
        }
        self.weather_data = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=self.weather_apiparams).json()
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # checking if conditions are unsafe for driving by checking weather ids in the next 12 hours
    def should_take_bus(self):
        for i in range(0, 12):
            hourly_forecast = self.weather_data["hourly"][i]['weather'][0]['id']
            weather_desc = self.weather_data["hourly"][i]['weather'][0]['description']
            if hourly_forecast == 503 or hourly_forecast == 504 or hourly_forecast == 511 or hourly_forecast == 616 \
                    or hourly_forecast == 622:
                return [True, weather_desc]
        return [False, weather_desc]

    # texts the user if conditions are unsafe for driving
    def text_user(self):
        should_take_bus = self.should_take_bus()[0]
        forecast = self.should_take_bus()[1]
        # sending a message based on the weather conditions
        message_body = f'The weather forecast for today is "{forecast}". Road conditions are not suitable for driving, ' \
                           f'please take the bus 🚌 if possible so you can be safe and help save the planet! 🌳'
        if should_take_bus == True:
            message = self.client.messages.create(
                body=message_body,
                from_='+13233104492',
                to=self.user.phone
            )
            print(message.status)