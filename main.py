import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movie_titles = [tag.getText() for tag in movie_tags]
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")


