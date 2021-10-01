import nltk
from pathlib import Path
import requests
from bs4 import BeautifulSoup as bs4
import os 
import json
import re
import sqlite3

WIKI_DIR = "https://en.wikipedia.org/wiki/"
test_correct_url_ = "https://en.wikipedia.org/wiki/Wiki"
test_wrong_url_ = "https://en.wcor.org/wiki/Wiki"

"""
Please be careful when trying to decide on a location for /DataFile.

It will automatically be created in the parent directory of your current 
execution directory.

You can modify the designated location for your /DataFile by 
changing the PARENT_DIR variable.
"""
PARENT_DIR = "../DataFile/"
TENSE_DIR = "LinkFile/"
RAKE_DIR = "RAKE/"
PAGE_DIR = "WikiPageDocument/"
TOKEN_DIR = "TokenData/"

class Checker:
    def __init__(self, topic="", parentdir=PARENT_DIR):
        self.wiki_path = WIKI_DIR
        self.url = []
        self.parentdir = parentdir
        self.tensedir = os.path.join(parentdir, TENSE_DIR)
        self.tocdir = os.path.join(parentdir, RAKE_DIR)
        self.wikidir = os.path.join(parentdir, PAGE_DIR)
        self.tokendir = os.path.join(parentdir, TOKEN_DIR)
        self.topic = topic
        
    def checkFilePath(self):
        dir_list = [self.tensedir, self.tocdir, self.tokendir, self.wikidir]
        print("Checking Directory...\n")
        try:
            print(self.parentdir)
            os.umask(0)
            os.makedirs(self.parentdir, mode=0o777)
            print("Parent directory for data files created!\n")
        except FileExistsError:
            print("Parent Folder exists!")
            pass
        
        for path in dir_list:
            try:
                os.mkdir(path)
                os.path.join(path, self.topic)
                
            except FileExistsError:
                print("Directory '%s' already exists" %path)
                pass
    
    def testTimeOut(self, request, topic):
        try:
            requests.get(request)
        except TimeoutError:
            print("Timeout Error! Retry again later.")
            exit()
            

    def checkReqPackage(self):
        requirements = [
            'punkt',
            'universal_tagset', 
            'averaged_perceptron_tagger', 
            'stopwords'
        ]
        pack = nltk.downloader.Downloader()
        for mod in requirements:
            if(pack.is_installed(mod)):
                pass
            else:
                print("\nNot all the required nltk packages are installed!\n")
                print("Downloading uninstalled content....\n")
                pack.download(info_or_id=mod)
                print("Download complete!\n")
        print("All SET!\n")
    
    
class Crawler(Checker):
    def __init__(self, filename):
        Checker.__init__(self, filename)
        self.WIKILINK = self.wiki_path + self.topic
        self.topicList = []
        self.listofcontents = os.path.join(self.tensedir, self.topic + ".json")
        
    def requestForHTML(self):
        try:
            url = requests.get(self.WIKILINK)
            
        except (ConnectionError, TimeoutError):
            print("You have a network problem. Recheck your connection.\n")
            exit()
            
            
        html = url.text
        soupify = bs4(html, 'html.parser')
        
        return soupify
    
    def vagueLinks(self):
        soupify = self.requestForHTML()
        
        try:
            # for "...For other uses..."
            vague = soupify.find(role="note").find_all("a")
        except AttributeError as aerror:
            # print("Error Occured: >> {}".format(aerror))
            #  for "...may refer to:..."
            vague = soupify.find(class_="mw-parser-output").find("ul", recursive=False).find_all("li")
        print("The topic has other similar Wiki Links\nTry the following topics for more info. >>\n")
        for i in vague:
            print("{}\n".format(i.text))
        
        


    def requestPageData(self):
        soupify = self.requestForHTML()
        parags = soupify.find(
            id="mw-content-text"
            ).find(
            class_="mw-parser-output"
            ).find_all(
                "p", recursive=False
                )
        
        ### Crawls for url links on Topic wiki page
        for link in parags:
            if(link is not None):
                self.topicList.append(link.find_all('a'))
        tag_file = open(self.listofcontents, 'w+', encoding='utf-8')
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

    def requestWikiPageDoc(self):
        soupify = self.requestForHTML()
        get_document_content = soupify.find(id="mw-content-text").find(class_="mw-parser-output")
        tags = get_document_content.find_all(['p','h2','h3'])
        
        fname = os.path.join(self.wikidir, self.topic + ".txt")
        print(fname)
        f = open(fname, 'w+')

        for tag in tags:
            text = tag.text
            try:
                f.write(text)
                f.write('\n')
            except:
                pass
            
        f.close()
            

class Parser(Crawler):
    def __init__(self, main_topic):
        Crawler.__init__(self, main_topic)
    
    def checkRequirements(self):
        self.checkReqPackage()
        self.checkFilePath()
        self.requestPageData()
        # self.requestTOC()
        self.requestWikiPageDoc()
        self.vagueLinks()
        # self.requestTP()

    def loadJson(self):
        with open(self.listofcontents, 'r', encoding='utf-8') as jsonf:
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
                print("TITLE: {} ==> WIKI LINK: {} \n\n".format(data['title'], WIKI_DIR + data['link'][6:]))
            except KeyError:
                pass
