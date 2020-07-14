import nltk
from pathlib import Path
import requests
from bs4 import BeautifulSoup as bs4
import os 
import json
import re
import sqlite3

wiki_url = "https://en.wikipedia.org/wiki/"
test_correct_url_ = "https://en.wikipedia.org/wiki/Wiki"
test_wrong_url_ = "https://en.wcor.org/wiki/Wiki"

"""
Please be careful when trying to decide on a location for /DataFile.

It will automatically be created in the parent directory of your current 
execution directory.

You can modify the designated location for your /DataFile by 
changing the parent_dir variable.
"""
parent_dir = "../DataFile/"
tense_dir = "TenseFile/"
toc_dir = "RAKE/"
wiki_dir = "WikiPageDocument/"
token_dir = "TokenData/"

class Checker:
    def __init__(self, topic="", parentdir=parent_dir):
        self.wiki_path = wiki_url
        self.url = []
        self.parentdir = parentdir
        self.tensedir = os.path.join(parentdir, tense_dir)
        self.tocdir = os.path.join(parentdir, toc_dir)
        self.wikidir = os.path.join(parentdir, wiki_dir)
        self.tokendir = os.path.join(parentdir, token_dir)
        self.topic = topic
        
    def checkFilePath(self):
        dir_list = [self.tensedir, self.tocdir, self.tokendir, self.wikidir]
        print("Checking Directory...\n")
        try:
            print(self.parentdir)
            os.mkdir(self.parentdir)
            print("Parent directory for data files created!\n")
        except FileExistsError:
            print("Parent Folder exists!")
            pass
        
        for path in dir_list:
            try:
                os.mkdir(path)
                file_path = os.path.join(path, self.topic)
                
            except FileExistsError:
                print("Directory '%s' already exists" %path)
                pass
    
    def testTimeOut(self, request, topic):
        try:
            requests.get(request)
        except TimeoutError:
            print("Timeout Error. You fucking better spend more of that Lincoln dollars getting a new home network!@")
            

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
        
    def requestPageData(self):
        soupify = self.requestForHTML()
        parags = soupify.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p", recursive=False)
        
        ### Crawls for url links on Topic wiki page
        for link in parags:
            if(link is not None):
                self.topicList.append(link.find_all('a'))
        tag_file = open(self.listofcontents, 'a+', encoding='utf-8')
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

#TODO: Table of contents parsing for creating Big BulletPoints!
    def requestTOC(self):
        soupify = self.requestForHTML()
        table_of_contents = soupify.find(id='mw-content-text').find(class_='mw-parser-output').find(id='toc')
        
        ### Crawls for TOC on a wikipediac page
        toc_list_ul = []
        toc_list = []
        try:
            for toc in table_of_contents.find_all('li'):
                # print(toc.ul)
                for x in toc.get_text().split('\n'):
                    if(x != ""):
                        toc_list_ul.append(x)
        except AttributeError:
            pass

        for i in toc_list_ul:
            if(i not in toc_list):
                toc_list.append(i)
                
        temp = [ [] for _ in range(len(toc_list))] 
        for i in toc_list:
            index = int(i[0]) - 1
            temp[index].append(i)
        
# gets document content from desired topic

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
        self.requestTOC()
        self.requestWikiPageDoc()
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
                print("TITLE: {} ==> WIKI LINK: {} \n\n".format(data['title'], wiki_url + data['link']))
            except KeyError:
                pass
