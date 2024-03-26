import urllib.request

def myurllib(url):
    _url = url
    with urllib.request.urlopen(_url) as response:
        html_data = response.read()  # Returns data in bytes
        text = html_data.decode("utf-8")  # Decode to get text
    return text
def hello():
    print("myurlllib success")
