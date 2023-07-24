# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below

def verify_otp():

	username = request.form['username']
	password = request.form['password']

	if username == 'verify' and password = '12345':

        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='Enter mode of sending otp here')


    else:
    	return "Entered User ID or Password is wrong"







if __name__ == "__main__":
    app.run()

