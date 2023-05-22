import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
best_movies = response.text

soup = BeautifulSoup(best_movies, "html.parser")
all_movies = soup.find_all(class_="title")
movie_titles = []

for movie in all_movies:
    title = movie.getText()
    movie_titles.append(title)

movie_titles.reverse()
top_100_movies = movie_titles

# print(top_100_movies)

with open ("top_100_movies.txt", mode="w") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")
