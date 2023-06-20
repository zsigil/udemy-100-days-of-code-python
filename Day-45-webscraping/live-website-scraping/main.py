import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
titleline_anchors = soup.select(selector=".titleline>a")
titleline_anchor_texts = [el.getText() for el in titleline_anchors]
titleline_anchor_hrefs = [el.get("href") for el in titleline_anchors]
upvotes = [int(el.getText().split(' ')[0])
           for el in soup.find_all(name="span", class_="score")]

print(titleline_anchor_texts)
print(titleline_anchor_hrefs)
print(upvotes)


index = upvotes.index(max(upvotes))
print('index:', index)

print(titleline_anchor_texts[index])
print(titleline_anchor_hrefs[index])
print(upvotes[index])
