import nltk

class Processor():
    def __init__(self, topic_name="", folder_path="./WikiPageDocument/", file_extension=".txt"):
        self.file_path = folder_path + topic_name + file_extension
        
    def processor(self):
        
        with open(self.file_path, 'r') as file:
            content = file.readlines()
            content = [ct for ct in content if ct != "\n"]
            tokenizer = nltk.tokenize.word_tokenize
            content_matrix = [[tokenizer(line)] for line in content]
            print(content_matrix[0])
        file.close()