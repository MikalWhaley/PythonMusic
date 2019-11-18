import requests
import json
from key import key

# Misuxmatch API linked to track.search method
trackSearch = "https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&q_lyrics=we%20will%20rock%20you&quorum_factor=1" 
lyricSearch = "&q_lyrics="

userInput = input("Enter Lyrics: ")

querystring = {
	"q" : lyricSearch+userInput
}
# response = requests.get(trackSearch+apikey)
response = requests.request("GET", trackSearch+key+querystring['q'])

print(response.url)

# Gets rid of 'callback()' that was included in the api callback
responseText = response.text[9:-2]
json_data = json.loads(responseText)
print(json_data)

print(json_data["message"]["body"]["track_list"][0]["track"]["track_name"])