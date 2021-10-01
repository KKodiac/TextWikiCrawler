"""
    Module for text extracting most relevant text/sentence/words from the
    Topic searched on Wikipedia that was scraped.

    Using RAKE(Rapid Automatic Keyword Extraction) algorithm.
    Implemented by csurfer(https://github.com/csurfer/rake-nltk/blob/master/rake_nltk/rake.py)
"""

from processor import Processor
from rake_nltk import Rake
import json

class Extractor:
    def __init__(self, topic, MIN_LENGTH=1, MAX_LENGTH=4):
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
            pair.append(dict(temp))
        print()
        json.dump(pair, RAKE_file, indent=4)