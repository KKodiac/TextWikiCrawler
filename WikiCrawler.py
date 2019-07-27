import nltk
from pathlib import Path 
import nltk 
import requests
from bs4 import BeautifulSoup as bs4
from os import mkdir

test_correct_url_ = "https://en.wikipedia.org/wiki/Wiki"
test_wrong_url_ = "https://en.wcor.org/wiki/Wiki"


class Checker:
    def __init__(self, DIR="./DataFile/",filename=""):
        self.url = []
        self.DIR = DIR
        self.filename = filename
        self.FILEPATH = self.DIR + self.filename
    def checkReqPackage(self):
        requirements=['punkt', 'universal_tagset', 'averaged_perceptron_tagger']
        pack = nltk.downloader.Downloader()
        for mod in requirements:
            if(pack.is_installed(mod)):
                pass
            else:
                print("Not all the required nltk packages are installed!\n")
                print("Downloading uninstalled content....\n")
                pack.download(info_or_id=mod)
                print("Download complete!\n")
        print("All SET!\n")
            
    def checkFilePath(self):
        dat_file = Path(self.FILEPATH)
        try:
            mkdir(self.DIR)
            new_file = open(self.FILEPATH, 'a')
        except FileExistsError:
            print("File already exists.\n")
            pass
        else:
            new_file = open(self.FILEPATH, 'w+')
            new_file.write("This file is created to store crawled data\n")
            new_file.close()
        

class Crawler:
    def __init__(self, topic=""):
        self.topic = topic
        self.wiki_path = "https://en.wikipedia.org/wiki/"
        self.WIKILINK = self.wiki_path + self.topic
        self.parags = []
    def requestForHTML(self):
        try:
            url = requests.get(self.WIKILINK)
        except ConnectionError:
            print("You have a network problem. Recheck your connection.\n")
            exit()
        except TimeoutError:
            print("Your connection timed out.\n")
            exit()
        html = url.text
        soupify = bs4(html, 'html.parser')
        print(soupify)
        parags = soupify.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p", recursive=False)
        print(parags)
        atags = parags.find("a", recursive=False)
        print(atags)


class Parser:
    pass
    