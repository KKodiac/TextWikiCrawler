import nltk
import re
import matplotlib.pyplot as plt
import csv

class Processor():
    def __init__(self, topic_name="", bfolder_path="./DataFile/WikiPageDocument/", bfile_extension=".txt"
                    , afolder_path="./DataFile/TokenData/", afile_extension=".csv"):
        self.btoken_file_path = bfolder_path + topic_name + bfile_extension
        self.atoken_file_path = afolder_path + topic_name + afile_extension
        
    def processor(self):
        
        with open(self.btoken_file_path, 'r') as file:
            content = file.readlines()
            content = [re.sub('[^A-Za-z0-9]+', ' ', ct) for ct in content]
            tokenizer = nltk.tokenize.word_tokenize
            content_matrix = [tokenizer(line) for line in content]
            stop_words_set = set(nltk.corpus.stopwords.words('english'))
            
            total_sent = [words.lower() for sent in content_matrix for words in sent if not words in stop_words_set]
            # print(total_sent)
            fdist = nltk.probability.FreqDist(total_sent) 
            print(fdist["korea"])
            
            print(fdist.keys())
            print(fdist.items())
            # fdist.plot(30)
            # plt.show()
                
        file.close()
        
        with open(self.atoken_file_path, 'w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Words", "Word Frequency"])
            for key, value in fdist.items():
                writer.writerow([key, value])

        """ TO read back
        with open(self.atoken_file_path, 'r') as file:
            reader = csv.reader()
            fdist_dict = dict(reader)
        """
        file.close()
