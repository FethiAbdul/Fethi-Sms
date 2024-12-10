import urllib.request
import json


# function to get weather details
def get_weather(city):
  
  api='c6751c329196552d49c5e957e785a301'
  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
  request= urllib.request.urlopen(url)
  result = json.loads(request.read())
  # gets the temperature from the result and convers it to celsius
  temp_c =round(result['main']['temp']-273.15,2)
  return temp_c            # returns the temperature in celsius
