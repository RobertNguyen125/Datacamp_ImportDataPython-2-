# request -> open ->respone -> read()
from urllib.request import urlopen, Request


url = "http://www.datacamp.com/teach/documentation"

request = Request(url)

#send request and catch the response
response = urlopen(request)

#extract the response:html
html = response.read()
#print(html)
#print(type(response))
response.close()

#using requests package
import requests
url = "http://www.datacamp.com/teach/documentation"

r = requests.get(url)

text = r.text
print(text)
