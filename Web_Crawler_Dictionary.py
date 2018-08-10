"""
This program uses webcrawling to give you most needed information along with
some of the knowledge that you might also need to know alongside of the one
you searched for.
Hopefully will add machine learning part of the code for more accurate results
And also sort the results in SQL databases using django***

"""

import time
import sys
from bs4 import BeautifulSoup as bs
import requests as rq
import nltk
import re
import urllib.parse
print(sys.executable)
print(sys.version)

# url link to webpages that will be excessed
html_container = ["https://en.wikipedia.org/wiki/Android_(operating_system)"]
text_handler = "text_data.cvs"
# crawls through wikipedia page and looks for the first links to jump into


def viewNext(htmlContainer):
    print(htmlContainer)
    try:
        url = rq.get(htmlContainer[-1])
    except Exception:
        print("ConnectionError: Stop overflowing the site with traffic, Dimwit")
        print("Shutting off...")
    html = url.text
    soup = bs(html, 'html.parser')
    div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    ptags = div.find_all("p", recursive=False)
    # checks for any <p class="mw-empty-elt" which is just an empty p tag(not helpful
    # data for data scrapping)and inside the second while loop, it checks for any links that lead to
    # pronounciation pages(also not helpful)
    ptagCount = 0
    while(True):
        if(ptags[ptagCount].text != "\n"):
            atagCount = 0
            atags = ptags[ptagCount].find_all("a", recursive=False)
            ahref = atags[atagCount]['href']
            # print(atags)
            while('/wiki/Help:' in ahref):
                atagCount += 1
                ahref = atags[atagCount]['href']
            # print(ahref)
            atagCount = 0
            break
        else:
            ptagCount += 1

    # print(ahref)
    next_url = urllib.parse.urljoin("https://en.wikipedia.org", ahref)
    html_container.append(next_url)
    return True
# reads first few sentences of content and saves it in data
# splits wordCrawl data into bits in arrays
# use this data to tag more related and accurate information


def wordCrawl(htmlContainer):
    failcount = 0
    file = open(text_handler, 'w')
    for i in htmlContainer:
        word_bank = list()
        try:
            url = rq.get(i)
        except Exception:
            print("ConnectionError: Stop overflowing the site with traffic, Dimwit")
            print("Shutting off...")
            sys.exit(0)
        html = url.text
        soup = bs(html,  'html.parser')
        ptag = soup.find(id="mw-content-text").find_all("p")
        tag = ptag[failcount].get_text()
        while(tag == "\n"):
            failcount += 1
            tag = ptag[failcount].get_text()
        words = re.sub('[^A-Za-z]+', ' ', tag)  # filtering out special characters
        token = nltk.word_tokenize(words)
        tagged = nltk.pos_tag(token, tagset='universal')
        for element in tagged:
            word, typeof = element
            if(typeof in ['NOUN', 'VERB', 'NUM', 'ADJ']):
                word_bank.append(element)

        # to append url link that leads to the word and tense information
        urlpath = urllib.parse.urlparse(i).path
        for words in sorted(word_bank, key=lambda word: word[1]):
            for ch in ['\'', '(', ')', ' ']:
                if(ch in words):
                    words = words.replace(ch, "")
            word, tense = words
            file.write("{},{},{}".format(word, tense, urlpath))
            file.write("\n")
    file.close()


def mainCrawl():
    crawl_count = 2  # number of crawling operations
    while(viewNext(html_container)):
        print("Wikipeidia Crawling... Number of Crawling left ({})".format(crawl_count))
        crawl_count -= 1
        time.sleep(2)
        if(crawl_count == 0):
            print("Done...!")
            break
    wordCrawl(html_container)


mainCrawl()
