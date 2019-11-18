import requests
import json
from key import key

# Misuxmatch API linked to track.search method
trackSearch = "https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&q_lyrics=we%20will%20rock%20you&quorum_factor=1" 

# response = requests.get(trackSearch+apikey)
response = requests.request("GET", trackSearch+key)
print("Musixmatch lyrics API call: " + trackSearch+key + "\n")

print(response.status_code)
# Gets rid of 'callback()' that was included in the api callback
responseText = response.text[9:-2]
json_data = json.loads(responseText)
print(json_data)