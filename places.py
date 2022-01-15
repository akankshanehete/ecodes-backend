from apitokens import *
import geopy
from user import User
from geopy.geocoders import Nominatim



class Places:
    def __init__(self, user: User):
        self.geolocator = Nominatim(user_agent='Ecodes')
        self.location = self.geolocator.reverse(f"43.591290, -79.650250")


user1 = User('Akanksha Nehete', '299 E Craig Street, Tallulah, LA', '+16477676905')
place_user1 = Places(user1)
print(place_user1.current_address)




