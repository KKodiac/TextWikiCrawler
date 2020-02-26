import boto3 
import json
from os import path
from sys import argv

file_dir = '../DataFile/WikiPageDocument'

class Processor:
    def __init__(self, filename=""):
        self.fname = filename
        
    def comprehend(self):
        comp= boto3.client(service_name='comprehend', region_name='us-east-1') 
        fpath = path.join(file_dir, self.fname)
        print(fpath)
        with open(fpath, 'r') as file:
            # Get entire page text
            sample = file.readlines()
            # Get page text in list format
            
            
        comped = comp.detect_key_phrases(Text=sample[6], LanguageCode='en')
        dumped = json.dumps(comped, sort_keys=True, indent=4)
        
        file.close()
        
        with open("dump.json", 'w+') as f:
            loaded = json.loads(dumped)
            json.dump(loaded, f, sort_keys=True, indent=4)
        
        f.close()
        
        return dumped
        
    def processor(self):
        comp = self.comprehend()
        
        pass
        
    
    def show(self):
        comp = self.comprehend()
        print(comp)
            
        
if __name__ == '__main__':
    param_topic = argv[1]
    file_name = param_topic + ".txt"
    print(file_name)
    processor = Processor(file_name)
    processor.show()
    
#TODO: 