from bs4 import BeautifulSoup as bs4
import requests


url = requests.get('https://en.wikipedia.org/wiki/United_States')
html = url.text
soupify = bs4(html, 'html.parser')
cleantext = bs4(html,'html.parser').text
get_document_content = soupify.find(id="mw-content-text").find(class_="mw-parser-output")

# print(get_document_content.text)
tag = get_document_content.find_all(['p','h2', 'h3'])
for n,i in enumerate(tag):
    print(i.text)
    print("SKIPPPPPPP\n")

# ptags = get_document_content.find_all('p')
# for p in ptags:
#     print(ptags.text)