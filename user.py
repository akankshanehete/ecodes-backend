import geocoder

class User:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone
        # gets the current latitude and longitude of user based on their IP address
        self.current_lat = geocoder.ip('me').latlng[0]
        self.current_lng = geocoder.ip('me').latlng[1]

class Places(User):
    def __init__(self):
        super.__init__()
