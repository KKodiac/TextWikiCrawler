"""
    Module for text extracting most relevant text/sentence/words from the
    Topic searched on Wikipedia that was scraped.

    Using RAKE(Rapid Automatic Keyword Extraction) algorithm.
    Implemented by csurfer(https://github.com/csurfer/rake-nltk/blob/master/rake_nltk/rake.py)
"""

from .Processor import *
from rake_nltk import Rake

class Comprehend:
    def __init__(self, topic, MIN_LENGTH=2, MAX_LENGTH=10000):
        self.proc = Processor(topic)
        self.raker = Rake(min_length=MIN_LENGTH, max_length=MAX_LENGTH)

    def extract_keywords(self):
        self.proc.processor()
        file = open(self.proc.btoken_file_path, 'r')
        text = file.read()
        self.raker.extract_keywords_from_text(text)
        file.close()

    def extract_keywords_with_scores(self):
        text_with_scores = self.raker.get_ranked_phrases_with_scores()

        return text_with_scores
