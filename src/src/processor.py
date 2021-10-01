"""This processor is for simple content analyzing. 
    Processor() Class will output an .csv file with
    - Word in content, 
    - How frequently the word appears in the text
    - Part of speech that the word belongs to
    - Lastly, visualization of you output
    
    For Advanced content parsing, use ProcessorComprehend.py.
"""

import nltk
import re
import csv
from os import path
from ast import literal_eval
#TODO: Modify permenant file path to something scalable

class Processor():
    def __init__(
        self, 
        topic_name="", 
        bfolder_path="../DataFile/WikiPageDocument/", 
        bfile_extension=".txt", 
        afolder_path="../DataFile/TokenData/", 
        afile_extension=".csv"):

        self.btoken_file_path = path.join(
            bfolder_path,topic_name+bfile_extension
            )
        self.atoken_file_path = path.join(
            afolder_path,topic_name+afile_extension
            )
    
    def tag_list_make(self, list):
        tag_list = nltk.pos_tag(list.keys())
        cnt = list.items()

        keys = [tags[0].lower() for tags in tag_list]        
        freq = [freq[1] for freq in cnt]
        tag_list = [tags[1] for tags in tag_list]
        
        return keys, freq, tag_list
    
    def processor(self):
        _stopwords = open('_stopwords/_stopwords')
        _stopwords_text = _stopwords.read()
        with open(self.btoken_file_path, 'r') as file:
            content = file.readlines()
            content = [re.sub('[^A-Za-z0-9]+', ' ', ct) for ct in content]
            tokenizer = nltk.tokenize.word_tokenize
            content_matrix = [tokenizer(line) for line in content]
            stopwords_set = nltk.corpus.stopwords.words('english')
            stopwords_set.append(literal_eval(_stopwords_text))
            
            total_sent = [words.lower() for sent in content_matrix for words in sent if not words in stopwords_set]
            fdist = nltk.probability.FreqDist(total_sent) 
            keys, freq, tag_list = self.tag_list_make(fdist)
                
        file.close()
        
        with open(self.atoken_file_path, 'w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Words", "Word Frequency", "Part of Speech"])
            for cnt in range(len(fdist)-1):
                writer.writerow([keys[cnt], freq[cnt], tag_list[cnt]]) 
        
        file.close()
        
        return fdist
    

    def graph_plot(self):
        freqdist = self.processor()
        freqdist.plot()
        