#This is used separately from the rest of the project to obtain HTML
# used for analysis and planning for the rest of the project

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://stathead.com/football/vs/josh-allen-vs-jordan-love"

response = requests.get(base_site)
print(response) #200 is good, 404 is bad

html = response.content

soup = BeautifulSoup(html, "html.parser")

with open('allen_love_h2h.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))