import urllib.request # get data from url
import json #
import random

# fuction to get hp character details
def get_char():
  url='https://hp-api.herokuapp.com/api/characters'
  # opens the url and reads the data
  request= urllib.request.urlopen(url)
  result = json.loads(request.read())

  #print(result)
  #generates a random number between 1 and 40
  char = random.randint(1,40) 
  print(char)
  #check if the character is wizard key has a value of true
  if result[char]["wizard"] == True:
    return f"{result[char]['name']} is in the house Wizard and the name of the actor {result[char]['actor']} and the image of the character is {result[char]['image']}"
  else:     # if the character is not wizard key has a value of false
    #retruns the name of the character and the actor name and image url
    return f"{result[char]['name']} is not in the house Wizard and the name of the actor {result[char]['actor']} and the image of the character is {result[char]['image']}"