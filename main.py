import requests
import json
from key import key
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

song_names = []
album_names = []
artist_names = []
track_id = []
cover_art = []

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

	global song_names
	global album_names
	global artist_names
	global track_id
	global cover_art

	if len(song_names) != 0:
		song_names.clear()
	elif len(album_names) != 0:
		album_names.clear()
	elif len(artist_names) != 0:
		artist_names.clear()
	elif len(track_id) != 0:
		track_id.clear()
	elif len(cover_art) != 0:
		cover_art.clear()

	# Appends all songs, album, and artist names in separate lists
	for i in range(len(json_data["message"]["body"]["track_list"])):
		song_names.append(json_data["message"]["body"]["track_list"][i]["track"]["track_name"])
		album_names.append(json_data["message"]["body"]["track_list"][i]["track"]["album_name"])
		artist_names.append(json_data["message"]["body"]["track_list"][i]["track"]["artist_name"])
		track_id.append(json_data["message"]["body"]["track_list"][i]["track"]["track_id"])

	# Uses last.fm API to get album artwork
	for i in range(len(album_names)):
		art_Search = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=e88853d03b96eefc3b794d51cbe626ff&artist=" + artist_names[i] + "&album="  + album_names[i] + "&format=json"
		cover_response = requests.request("GET", art_Search)
		cover_data = json.loads(cover_response.text)

		# If Album is not found
		if (len(cover_data) == 3):
			cover_art.append('/static/placeholder.png')
		# If Album is there but no artwork
		elif(cover_data["album"]["image"][3]["#text"] == ""):
			cover_art.append('/static/placeholder.png')
		else:
			cover_art.append(cover_data["album"]["image"][3]["#text"])
	
	return render_template('results.html', song_names = song_names, album_names = album_names, artist_names = artist_names, cover_art = cover_art, track_id = track_id)

@app.route('/lyrics/<track>')
def lyrics(track):
	global song_names
	global album_names
	global artist_names
	global track_id
	global cover_art
	index = 0
	album = ""
	song = ""
	artist = ""
	cover = ""
	
	for id in track_id:
		if(id == int(track)):
			album = album_names[index]
			song = song_names[index]
			artist = artist_names[index]
			cover = cover_art[index]
		index += 1

	lyricsSearch = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?format=jsonp&callback=callback&track_id=" + str(track) + key
	lyrics_response = requests.request("GET", lyricsSearch)
	lyrics_responseText = lyrics_response.text[9:-2]
	lyrics_data = json.loads(lyrics_responseText)

	lyrics = lyrics_data['message']['body']['lyrics']['lyrics_body']
	return render_template('lyrics.html', lyrics = lyrics, album = album, song = song, artist = artist, cover = cover)




