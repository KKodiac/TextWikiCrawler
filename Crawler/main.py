from src.WikiCrawler import Parser
from src.Processor import Processor
from src.ExtractKeyword import Comprehend, ConnectSql
import argparse
import sys


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
