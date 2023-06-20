from bs4 import BeautifulSoup

with open('website.html', 'r', encoding='utf-8') as f:
    contents = f.read()
    # contents is str


# soup is object!!!
soup = BeautifulSoup(contents, 'html.parser')
all_anchor_elements = soup.find_all(name='a')

print(soup.title.name)  # "title"
print(soup.title.string)  # "Angela's Personal Site"
print(all_anchor_elements)


for el in all_anchor_elements:
    print(el.getText())
    print(el.get('href'))


heading = soup.find(name="h1", id="name")
print(heading)

# class is reserved keyword!
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a").get('href')
print(company_url)
