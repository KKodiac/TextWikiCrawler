import nltk
from pathlib import Path 
import nltk 
import requests
from bs4 import BeautifulSoup as bs4

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
        if(dat_file.exists()):
            pass
        else:
            new_file = open(self.FILEPATH, 'w+')
            new_file.write("This file is created to store crawled data\n")
            new_file.close()
        

class Crawler:
    def __init__(self, topic=""):
        self.topic = topic
