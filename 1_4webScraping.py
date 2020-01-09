#1: parsing HTML with BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

#oackage the request, send the request and catch the response: r
r = requests.get(url)

#extract the response as html: html_doc
html_doc = r.text

#create a BeautifulSoup subject from the html: soup
soup=BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
#print(pretty_soup)

#2: getting the text
guido_title = soup.title
print(guido_title)

guido_text = soup.get_text()
#print(guido_text)

#3: get the hyperlink
a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))
