import requests
import json
from key import key

# Musixmatch API linked to track.search method
trackSearch = "https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&quorum_factor=1&s_track_rating=desc"

# takes in input from user and appends it to querystring
user_input = input("Enter Lyrics: ")
querystring = "&q="+user_input


# response = requests.get(trackSearch+apikey)
response = requests.request("GET", trackSearch+key+querystring)

# Gets rid of 'callback(' and ');' that was included in the api callback string
responseText = response.text[9:-2]

# loads the response text as json data
json_data = json.loads(responseText)

