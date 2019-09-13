import nltk
from pathlib import Path
import nltk
import requests
from bs4 import BeautifulSoup as bs4
from os import mkdir
import json
import re
import sqlite3

wiki_url = "https://en.wikipedia.org"
test_correct_url_ = "https://en.wikipedia.org/wiki/Wiki"
test_wrong_url_ = "https://en.wcor.org/wiki/Wiki"

dir = "./Crawler/DataFile/"
word_dir = "./Crawler/TenseFile"

class Checker:
    def __init__(self, DIR=dir, filename="", WORD_DIR=word_dir):
        self.url = []
        self.DIR = DIR
        self.filename = filename
        self.FILEPATH = self.DIR + self.filename
        self.FILEPATH2 = self.WORD_DIR + self.filename

    def checkReqPackage(self):
        requirements = [
            'punkt', 'universal_tagset', 'averaged_perceptron_tagger'
        ]
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
        try:
            mkdir(self.DIR)
            mkdir(self.WORD_DIR)
        except FileExistsError:
            print("File already exists.\n")
            pass
        else:
            print("File created. \n")
        new_file = open(self.FILEPATH, 'w+')
        new_file2 = open(self.FILEPATH2, 'w+')
        new_file.close()
        new_file2.close()


class Crawler:
    def __init__(self, topic=""):
        self.fileURL = dir + topic + ".json"
        self.topic = topic
        self.wiki_path = "https://en.wikipedia.org/wiki/"
        self.WIKILINK = self.wiki_path + self.topic
        self.parags = []
        self.topicList = list()

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
        parags = soupify.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p", recursive=False)
        
        ### Crawls for url links on Topic wiki page
        for link in parags:
            if(link is not None):
                self.topicList.append(link.find_all('a'))
        tag_file = open(self.fileURL, 'a+', encoding='utf-8')
        tag_file.write('[')
        id_count = 0
        for i in self.topicList:
            for a in i:
                if(re.match('/wiki/*', a.attrs['href']) is not None):
                    id_count+=1
                    data = {
                        'id': id_count,
                        'title': a.attrs['title'],
                        'link': a.attrs['href']
                    }
                    json.dump(data, tag_file)
                    tag_file.write(',')
        tag_file.write('{}]')
        tag_file.close()

            
class Parser(Crawler, Checker):
    def __init__(self, main_topic):
        fname = main_topic+".json"
        Checker.__init__(self, filename=fname)
        Crawler.__init__(self, main_topic)
    
    def checkRequirements(self):
        self.checkReqPackage()
        self.checkFilePath()
        self.requestForHTML()

    def loadJson(self):
        with open(self.fileURL, 'r', encoding='utf-8') as jsonf:
            datas = jsonf.read()
            datal = json.loads(datas) # datal is a list
        return datal

    ### FOR TEST RETURNS ###
    def returnData(self):
        print("----------------------------------\n")
        print("HERE ARE THE KEY WORD RESULTS\n")
        print("----------------------------------\n")
        for data in self.loadJson():
            try:
                print("TITLE: {} ==> WIKI LINK: {} \n\n".format(data['title'], wiki_url + data['link']))
            except KeyError:
                pass

    def addToSQL(self):
        SQLPATH = "./Web/database.sqlite3"
        db = sqlite3.connect(SQLPATH)
        data = self.loadJson()
        columns = ['id', 'title', 'link']
        query = "INSERT OR IGNORE INTO notes_data(id,title,link) VALUES (?,?,?)"
        for d in data:
            try:
                keys = tuple(str(d[c]) for c in columns)
            except KeyError:
                pass
            c = db.cursor()
            c.execute(query,keys)
            db.commit()
        c.close()


