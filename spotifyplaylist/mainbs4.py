from bs4 import BeautifulSoup
import requests

date = input("Give the time machine a date in this format - YYYY-MM-DD : ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
reply = response.text

soup = BeautifulSoup(reply, "html.parser")
songs = soup.select("li ul li h3")
artists = soup.select("li ul li span")
song_list = [song.getText().strip('\n\t') for song in songs]
artists_list = [artist.getText().strip('\n\t') for artist in artists]

# print(song_list)
# print(artists_list)
