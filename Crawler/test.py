from bs4 import BeautifulSoup as bs4
import requests


url = requests.get('https://en.wikipedia.org/wiki/Yellow-faced_honeyeater')
html = url.text
soupify = bs4(html, 'html.parser')
parags = soupify.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p", recursive=False)
table_of_contents = soupify.find(id='mw-content-text').find(class_='mw-parser-output').find(id='toc')
# print(table_of_contents.find_all('li').extract())
toc_list_ul = []
toc_list = []
for n, toc in enumerate(table_of_contents.find_all('li')):
    # print(toc.ul)
    for x in toc.get_text().split('\n'):
        if(x != ""):
            toc_list_ul.append(x)

for i in toc_list_ul:
    if(i not in toc_list):
        toc_list.append(i)

temp = [ [] for _ in range(len(toc_list))]

for i in toc_list:
    index = int(i[0])-1
    temp[index].append(i)

cluster = [x for x in temp if x != []]

print(cluster)