import geocoder, googlemaps
from apitokens import *

class User:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone
        # user is initialized with 0 points to start
        self.points = 0
        # gets the current latitude and longitude of user based on their IP address
        self.current_lat = geocoder.ip('me').latlng[0]
        self.current_lng = geocoder.ip('me').latlng[1]

    def increment_points(self, increment_number):
        self.points += increment_number

    def subtract_points(self, decrement_number):
        self.points -= decrement_number



