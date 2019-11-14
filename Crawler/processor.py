import nltk
import requests
from bs4 import BeautifulSoup as bs4

class Processor:
    def __init__(self, page=""):
        self.page = page
        self.url = requests.get(self.page)
        
    def nlp_process(self):
        html = self.url.text
        soupify = bs4(html,'html.parser')
        paragraphs = []
        split_sentence = []
        content = soupify.find(class_="mw-parser-output").find_all('p')
        paragraphs = [text for text in content if text.get_text() != "\n"]
        split_sentence = [sent.split('. ') for sent in paragraphs]
        for i in split_sentence:
            for j in i:
                
        print(split_sentence)

p = Processor("https://en.wikipedia.org/wiki/Korea")
p.nlp_process()