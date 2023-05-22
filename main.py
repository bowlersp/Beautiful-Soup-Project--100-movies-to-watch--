import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
best_movies = response.text

soup = BeautifulSoup(best_movies, "html.parser")
movies = soup.find_all(class_="title")
movie_title = []

for movie_tag in movies:
    movie_title = movie_tag.getText()
    print(movie_title)
