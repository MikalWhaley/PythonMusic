import requests
# Misuxmatch API linked to track.search method
trackSearch = “https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&q_lyrics=we%20will%20rock%20you&quorum_factor=1”
response = requests.request(“GET”, trackSearch+apikey)
print(“Musixmatch lyrics API call: ” + trackSearch+apikey + “\n”)
print(response.status_code)
# data = response.json()
json_data = json.loads(response.text)
print(data)