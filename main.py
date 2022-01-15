from weathertexter import WeatherTexter
from user import User
from flask import Flask
from datetime import datetime

# creating a new user, the information that the user gives will be stored inside the specific user instance of User class
user1 = User('Akanksha Nehete', '299 E Craig Street, Tallulah, LA', '+16477676905')
weathertexter = WeatherTexter(user1)
bus = weathertexter.should_take_bus()
weathertexter.text_user()


app = Flask(__name__)

# home route (displaying the home page)
@app.route('/')
def hello_world():
    return 'home page'


@app.route('/scanqr')
def scan_qr_code():
    return "scan qr code"


@app.route('/login')
def login():
    return "login page"


@app.route('/dashboard')
def dashboard():
    return "points dashboard"

@app.route('/portfolio')
def portfolio():
    return "portfolio"



if __name__ == '__main__':
    app.run(debug=True)
    # activating debug mode will reload the server