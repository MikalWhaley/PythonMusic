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

#print(json_data) # gets everything
# print(json_data["message"]["body"]["track_list"][0]["track"]["track_name"])
# print(json_data["message"]["body"]["track_list"][0]["track"]["album_name"])
# print(json_data["message"]["body"]["track_list"][0]["track"]["artist_name"])
# print(json_data["message"]["body"]["track_list"][0]["track"]["primary_genres"]["music_genre_list"][0]["music_genre"]["music_genre_name"])
# print(json_data["message"]["body"]["track_list"][0]["track"]["primary_genres"]["music_genre_list"][1]["music_genre"]["music_genre_name"])
# print("\n")

print(response.url)

song_names = []
for i in range(7):
	song_names.append(json_data["message"]["body"]["track_list"][i]["track"]["track_name"])


album_names = []
for i in range(7):
	album_names.append(json_data["message"]["body"]["track_list"][i]["track"]["album_name"])

artist_name = []
for i in range(7):
	artist_name.append(json_data["message"]["body"]["track_list"][i]["track"]["artist_name"])

# genre_names = []
# for i in range(7):
# 	print("i",i)
# 	for j in range(2):
# 		print("j",j)
# 		genre_names.append(json_data["message"]["body"]["track_list"][i]["track"]["primary_genres"]["music_genre_list"][j]["music_genre"]["music_genre_name"])


# print(json_data["message"]["body"]["track_list"][1]["track"]["primary_genres"]["music_genre_list"][0]["music_genre"]["music_genre_name"])

# if (json_data["message"]["body"]["track_list"][1]["track"]["primary_genres"]["music_genre_list"][0]["music_genre"]["music_genre_name"])!:
# 	print("yep")
