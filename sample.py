import getAbstractFromWeb as abstract
    
fetching_html_text = abstract.myrequests("https://arxiv.org/abs/1706.03762")

text = abstract.html2text(fetching_html_text)

abstract_content = abstract.abstract_content(text)

print(abstract_content)