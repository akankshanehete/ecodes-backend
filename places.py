from apitokens import *
import googlemaps, time, openpyxl
import pandas as pd
from user import User



class Places:
    def __init__(self, user: User):
        self.distance = 2000
        self.map_client = googlemaps.Client(GOOGLE_API_KEY)
        self.current_lat = user.current_lat
        self.current_lng = user.current_lng


    def get_places_nearby(self, search_string):
        response = self.map_client.places_nearby(
            location=(self.current_lat, self.current_lng),
            keyword=search_string,
            radius=self.distance
        )
        business_list = []
        business_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

        while next_page_token:
            time.sleep(0.1)
            response = self.map_client.places_nearby(
                location=(self.current_lat, self.current_lng),
                keyword=search_string,
                radius=self.distance,
                page_token=next_page_token
            )
            business_list.extend(response.get('results'))
            next_page_token = response.get('next_page_token')
            place_list = pd.DataFrame(business_list)[['geometry', 'name', 'vicinity']]
            return place_list


user1 = User('Akanksha Nehete', '299 E Craig Street, Tallulah, LA', '+16477676905')
print(user1.current_lat, user1.current_lng)
user1_places = Places(user1)
place_list = user1_places.get_places_nearby('thrift store')
print(place_list)