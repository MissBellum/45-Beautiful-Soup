import html

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response_text = response.text

article = BeautifulSoup(response_text, "html.parser")
tags = article.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in tags]
movies = movie_list[::-1]

with open("watchlist.txt", "w") as watch_list:
    for movie in movies:
        watch_list.write(f"{movie}\n")

print(movie_list[::-1])
