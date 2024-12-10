# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client # import twilio to send sms
import random  # import random to get random number
from space import people_space # import people_space function from space.py
from weather import get_weather # import get_weather function from weather.py
from hp import get_char # import get_char function from hp.py
import json # import json to get data from api
from flask import Flask,render_template # import flask to create web app

app = Flask('app') # create flask app



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


#create a dictionery named student to store my information
student = {
    "fethi":{
        "name":"fethi",
        "course":"BAGC",
        "number":"+16476146409",
        "lucky" :random.randint(1,100),
        "location":"waterloo"
    } 
}


# iterate through the student dictionery and send sms 
for key,value in student.items():
    msg=f'Hello {value["name"].title()} your lucky number is {value["lucky"]} and the number of people in space are {people_space()} and the city {value["location"]} weather in your location {value["location"]} is:{get_weather(value["location"])} and the HP character details {get_char()}'

    #print sms message using twilio 
    print(msg)
    message = client.messages.create(
        body=msg,
        from_="+19387777019", # my twilio number
        to=value["number"], #Receiver number 
    )
    with open('message.json','w') as outfile: # saving the message in json file
        json.dump(message.sid,outfile)


    print(message.body)

# define the route for the root path
@app.route('/')
def hello_world():
  return render_template("index.html") # render the index.html file

# define a route for the /sms path
@app.route('/sms')
def send_sms():
  # this is where you will connect to the APIS and send the SMS
  return render_template("success.html")

app.run(host='0.0.0.0', port=8080) # run the app on port 8080

