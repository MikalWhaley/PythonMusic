import requests
import json
from key import key
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	if request.method == 'POST':
		user_input = request.form['message']
    
    # Musixmatch API linked to track.search method
	trackSearch = "https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&quorum_factor=1&s_track_rating=desc"
	querystring = "&q="+user_input

	# response = requests.get(trackSearch+apikey)
	response = requests.request("GET", trackSearch+key+querystring)

	# Gets rid of 'callback(' and ');' that was included in the api callback string
	responseText = response.text[9:-2]

	# loads the response text as json data
	json_data = json.loads(responseText)

	song_names = []
	album_names = []
	artist_names = []
	cover_art = []
	for i in range(len(json_data["message"]["body"]["track_list"])):
		song_names.append(json_data["message"]["body"]["track_list"][i]["track"]["track_name"])
		album_names.append(json_data["message"]["body"]["track_list"][i]["track"]["album_name"])
		artist_names.append(json_data["message"]["body"]["track_list"][i]["track"]["artist_name"])


	for i in range(len(album_names)):
		art_Search = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=e88853d03b96eefc3b794d51cbe626ff&artist=" + artist_names[4] + "&album="  + album_names[4] + "&format=json"
		cover_response = requests.request("GET", art_Search)
		data = json.loads(cover_response.text)

		# if(data["message"] == "Album not found"):
		# 	cover_art.append('/static/placeholder.png')
		# # 	cover_art.append(data["album"]["image"][3]["#text"])
		# else:
		# 	cover_art.append(data["album"]["image"][3]["#text"])



	# print(cover_art)
	# return data
	return render_template('results.html', song_names = song_names, album_names = album_names, artist_names = artist_names, cover_art = cover_art)





