from src.WikiCrawler import Parser
from src.Processor import Processor
from src.ExtractKeyword import Comprehend, ConnectSql
import argparse
import sys

CONFIG = {
    'user' : 'root',
    'password' : 'Suskyssc2',
    'host' : '127.0.0.1',
    'database' : 'dbkeywords',
    'raise_on_warning' : True
}

if __name__ == '__main__':
    param_topic=sys.argv[1]
    parser = Parser(param_topic)
    # #Required to run only when runnning the program the first time
    parser.checkRequirements()
    parser.returnData()
    
    
    parser = Processor(param_topic)
    parser.processor()    

    proc = Comprehend(param_topic)
    proc.extract_keywords()
    proc.load_to_data()

    sql = ConnectSql(config=CONFIG)