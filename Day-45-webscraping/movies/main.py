import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_text = response.text

soup = BeautifulSoup(website_text, 'html.parser')
titles = [el.getText() for el in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open('movies.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title)
        f.write('\n')
