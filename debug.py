import getAbstractFromWeb as mylib

# module1 : _requests <=> success
# fetching_html_text = mylib.myrequests("https://en.wikipedia.org/wiki/Kyushu_University")
fetching_html_text = mylib.myrequests("https://arxiv.org/abs/1706.03762")
# print(fetching_html_text)

# module2 : _urllib <=> fail
# fetching_text = mylib.myurllib("https://en.wikipedia.org/wiki/Kyushu_University")
# print(f"{fetching_text}")
# mylib.hello()



# module3 : _BeautifulSoup <=> fail
# fetching_text = mylib.mysoup("https://en.wikipedia.org/wiki/Kyushu_University")
# print(f"{fetching_text}")
# mylib.hi()

# module4 : _html2text
text = mylib.html2text(fetching_html_text)
# print(text)

# soup = BeautifulSoup(fetching_html_text, 'html.parser')
# text = soup.get_text()  

# Fetching only "Abstract:" content from arXiv <=> success
abstract_content = mylib.abstract_content(text)
print(abstract_content)



