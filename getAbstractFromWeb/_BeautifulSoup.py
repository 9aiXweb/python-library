import requests
from bs4 import BeautifulSoup

def mysoup(url):
    _url = url
    response = requests.get(_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for paragraph in soup.find_all('p'):
        return paragraph.text
    
def hi():
    print("mysoup success")
