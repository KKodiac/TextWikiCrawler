import nltk
import matplotlib.pyplot as plt


class Processor():
    def __init__(self, topic_name="", folder_path="./WikiPageDocument/", file_extension=".txt"):
        self.file_path = folder_path + topic_name + file_extension
        
    def processor(self):
        
        with open(self.file_path, 'r') as file:
            content = file.readlines()
            content = [ct for ct in content if ct != "\n"]
            tokenizer = nltk.tokenize.word_tokenize
            content_matrix = [tokenizer(line) for line in content]
            print(content_matrix[0])
            
            total_sent = []
            for n,sent in enumerate(content_matrix):
                for words in sent:
                    total_sent.append(words.lower())
                
            fdist = nltk.probability.FreqDist(total_sent) 
            print(fdist.most_common(15))
            # fdist.plot()
            # plt.show()
            # TODO: REMOVE STOPWORDS!!!!
        file.close()