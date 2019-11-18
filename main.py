import requests
import json
from key import key

# Misuxmatch API linked to track.search method
trackSearch = "https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&quorum_factor=1"

# takes in inout from user and appends it querystring
user_input = input("Enter Lyrics: ")
querystring = "&q="+user_input


# response = requests.get(trackSearch+apikey)
response = requests.request("GET", trackSearch+key+querystring)
print(response.url)
print()

# Gets rid of 'callback()' that was included in the api callback
responseText = response.text[9:-2]
json_data = json.loads(responseText)
