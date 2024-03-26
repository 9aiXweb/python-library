import requests

def myrequests(url):
    _url = url
    response = requests.get(_url)

    if response.status_code == 200:
        text = response.text
        return text
    else:
        return "Error fetching the page"

def test():
    print("Success")