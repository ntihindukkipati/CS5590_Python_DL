import requests
from bs4 import BeautifulSoup

def get_links():
    url = "https://catalog.umkc.edu/course-offerings/graduate/comp-sci/"
    sourceCode = requests.get(url)
    plainText= sourceCode.text
    soup=BeautifulSoup(plainText,"html.parser")
    print('**********************************************************************')
# Finding all the divs with class courseblock
    result = soup.find_all('div', {'class': 'courseblock'})
# getting and printing all the course names and corse descriptions from the scrapped code
    for c in result:
        result1 = c.find('span', {'class': 'code'}).text
        result2 = c.find('p', {'class': 'courseblockdesc'}).text
        print(result1)
        print(result2)

get_links()