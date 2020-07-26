"""
    Module for text extracting most relevant text/sentence/words from the
    Topic searched on Wikipedia that was scraped.

    Using RAKE(Rapid Automatic Keyword Extraction) algorithm.
    Implemented by csurfer(https://github.com/csurfer/rake-nltk/blob/master/rake_nltk/rake.py)
"""

from .Processor import Processor
from rake_nltk import Rake
import json
import mysql.connector as connector


class Comprehend:
    def __init__(self, topic, MIN_LENGTH=2, MAX_LENGTH=10000):
        self.proc = Processor(topic)
        self.raker = Rake(min_length=MIN_LENGTH, max_length=MAX_LENGTH)
        self.topic = topic
        
    def extract_keywords(self):
        self.proc.processor()
        file = open(self.proc.btoken_file_path, 'r')
        text = file.read()
        self.raker.extract_keywords_from_text(text)
        file.close()

    def extract_keywords_with_scores(self):
        text_with_scores = self.raker.get_ranked_phrases_with_scores()

        return text_with_scores

    def load_to_data(self):
        pair = list()
        text_score = self.extract_keywords_with_scores()
        RAKE_file = open("../DataFile/RAKE/"+self.topic+".json", 'w+')
        for c in text_score:
            temp = [("score", c[0]),("text", c[1])]
            # print(dict(temp))
            pair.append(dict(temp))
        print()
        json.dump(pair, RAKE_file, indent=4)
        # 
        # json.dump(text_score, RAKE_file, indent=2)
"""
import mysql.connector

config = {
  'user': 'scott',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
"""

class ConnectSql:
    def __init__(self, config={}):
        try:
            self.cnx = connector.connect(**config)
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR: 
                print("Database does not exist")
            else:
                print(err)
        self.close = self.cnx.close()
  
            

        