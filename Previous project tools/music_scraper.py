import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_site = "https://en.wikipedia.org/wiki/Music"

response = requests.get(base_site)
print(response) #200 is good, 404 is bad

html = response.content
print(html[:100])

soup = BeautifulSoup(html, "html.parser")

with open('Wiki_music_response.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

print(soup.find('head')) #Header of the HTML doc

print(soup.find('a')) #Returns only the first result (a link cause it's 'a')
print(soup.find_all('a')) #That's more like it 
links = soup.find_all('a')
print(len(links)) #That's a lotta links

table = soup.find('tbody') #Finds a table
table_data = table.find_all('td') #Splits up data
print(len(table_data))

print(table.parent) #Returns parent tag

print(soup.find('div', id = 'siteSub')) #Site subtitle

a = soup.find_all('a', class_ = 'mw-jump-link') #Find by class
print(a)

a = soup.find('a', attrs={'class':'mw-jump-link', 'href':'#bodyContent'})
print(soup.find('a', attrs={'class':'mw-jump-link', 'href':'#bodyContent'})) #Can use dictionary too

print(a['href'])
print(a['class'])
print(a.attrs) #Prints attributes
print(a.string)

p = soup.find_all('p')[2]
print(p.text) #Full paragraph, removes styles
print(p.string) #None

print(p.parent.text) #Prints all text on page
print(soup.text) #Prints JS code as well as the text

for s in p.strings:
    print(repr(s)) #Prints all raw strings, formatting gets a lil funky

for s in p.stripped_strings:
    print(repr(s)) #Slightly less funky

print(links) #Prints links, duh

#Getting url for a single link
link = links[28]
print(link)
print(link.string)
relative_url = link['href']
print(relative_url)
full_url = urljoin(base_site, relative_url)
print(full_url)

#Get them links
clean_links = [l for l in links if l.get('href') != None]
for l in clean_links:
    print(l)
relative_urls = [l.get('href') for l in clean_links]
for l in relative_urls:
    print(l)
full_urls = [urljoin(base_site, url) for url in relative_urls]
for l in full_urls:
    print(l)

#Internal link (Wikipedia links only)
internal_links = [url for url in full_urls if 'wikipedia.org' in url]
for l in internal_links:
    print(l)

#Practice challenge -- retrieve titles of all links, extract text of all h2 tags, extract and print footer text
titles = [l.string for l in clean_links if l.string != None]
for t in titles:
    print(t)

h2_tags = links = soup.find_all('h2')
h2_texts = [l.string for l in h2_tags if l.string != None]
for t in h2_texts:
    print(t)

footer = soup.find('footer')
footer_text = [l for l in footer.contents]
footer_text = footer.find_all('li')
for t in footer_text:
    print(t)