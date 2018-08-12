"""
This program uses webcrawling to give you most needed information along with
some of the knowledge that you might also need to know alongside of the one
you searched for.
Hopefully will add machine learning part of the code for more accurate results
And also sort the results in SQL databases using django***

"""

from bs4 import BeautifulSoup as bs
import requests
import nltk
import sys
import re
from urllib.parse import urljoin, urlparse
import time

print(sys.executable)
print(sys.version)


class Crawler:
    def __init__(self, container, handler):
        self.container = container
        self.handler = handler

    def checkLegit(self, ptags):
        # variable counting iterations when itering through list of ptags
        for pIter, p in enumerate(ptags):
            if(p.text != "\n"):
                aIter = 0
                atags = ptags[pIter].find_all("a", recursive=False)
                # if below throws an IndexError it means that it wasn't able to
                # find any atags in the current p tag
                try:
                    href = atags[aIter]['href']
                except IndexError:
                    print("Wasn't able to find any href links. Skipping loop.\n")
                    continue
                while('/wiki/Help:' in href):
                    aIter += 1
                    href = atags[aIter]['href']

                return href

    def getLinks(self):
        try:
            url = requests.get(self.container[-1])
        except Exception:
            print("Could not receive GET request from the website.")
            print("Re-check html container array")
            sys.exit(0)
        html = url.text
        soup = bs(html, 'html.parser')
        div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
        ptags = div.find_all("p", recursive=False)
        href = self.checkLegit(ptags)
        next_url = urljoin("https://en.wikipedia.org", href)
        # TODO: could have all the href links on the site in a list
        # and iter through THAT and get next_url, like a tree structure
        self.container.append(next_url)

    def partOfSpeech(self, tagged, word_list):
        for element in tagged:
            word, tense = element
            if(tense in ['NOUN', 'VERB', 'NUM', 'ADJ']):
                word_list.append(element)

    def categorize(self, urlpath, word_list, file):
        for words in sorted(word_list, key=lambda word: word[1]):
            for char in ['\'', '(', ')', ' ']:
                if(char in words):
                    words = words.replace(char, "")

            word, tense = words
            file.write("{},{},{} \n".format(word, tense, urlpath))

    def wordCrawl(self):
        print(self.container)
        file = open(self.handler, 'w')
        file.write("Word,Tense,Link")
        word_list = list()
        for link in self.container:
            try:
                url = requests.get(link)
            except Exception:
                print("ConnectionError: Get request denied.\n Request Overflow")
                print("Shutting off...")
                exit(1)
            html = url.text
            soup = bs(html, 'html.parser')
            ptags = soup.find(id="mw-content-text").find_all("p")
            # print(ptags)
            for ptag in ptags:
                if(ptag == "\n"):
                    print("Skipping \n's")
                    pass
                else:
                    tag = ptag.get_text()  # all the text from one <p>
            words = re.sub('[^A-Za-z0-9]+', ' ', tag)
            token = nltk.word_tokenize(words)
            tagged = nltk.pos_tag(token, tagset='universal')
            self.partOfSpeech(tagged, word_list)

            # to append url link that leads to the word and tense information
            urlpath = urlparse(link).path

            self.categorize(urlpath, word_list, file)
        file.close()


if __name__ == '__main__':
    count = 0
    iter_num = int(input("How many time would you want your crawler to execute:  "))
    link = str(
        input("Enter url of the topic you want to crawl(full link):"))
    container = []  # container for keeping track of urls
    # handler = "dictionary.csv"  # file for keeping track of words and its data
    container.append(link)
    crawler1 = Crawler(container, handler="data1.csv")
    ctime1 = time.time()
    while(count < iter_num):
        crawler1.getLinks()
        time.sleep(2)  # halt crawling(Robot.txt)
        print(container)
        count += 1
    ctime2 = time.time()
    print("How long it took to crawl: {} (s)".format(ctime2-ctime1))
    print("container", crawler1.container)
    wtime1 = time.time()
    crawler1.wordCrawl()
    wtime2 = time.time()
    print("How long it took to create csv file: {} (s)".format(wtime2-wtime1))
