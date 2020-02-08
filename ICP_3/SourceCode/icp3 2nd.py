import requests
from bs4 import BeautifulSoup     #importing all requied libraries
url="https://en.wikipedia.org/wiki/Deep_learning"   #storing url into url variable
code=requests.get(url)         #making a get request
text=code.text
soup=BeautifulSoup(text,"html.parser")
print("links")
print(soup.find_all('a'))      #printing all anchor tags
print("Title")
print(soup.title)             #printing title tags
print("href looping over a tag")
for l in soup.find_all('a'):                  #printing all urls without anchor tag
    print(l.get('href'))

