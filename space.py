import urllib.request # get data from url
import json # get json response

# function to get people in space
def people_space():
  url='http://api.open-notify.org/astros.json'
  request= urllib.request.urlopen(url) # opens the url and reads the data
  result = json.loads(request.read()) # converts the data to json
  #return the number of people in space
  return f"The number of people in the space are {result['number']}"