import re
from bs4 import BeautifulSoup

def html2text(html_text):
    _html_text = html_text
    text = re.sub('<[^<]+?>', '', html_text) 
    return text

def abstract_content(text):
    start_index = text.find("Abstract:") + len("Abstract:") 
    end_index = text.find("\n", start_index) 
    abstract = text[start_index:end_index].strip()
    return abstract
