import WikiCrawler
import argparse
import sys

if __name__ == '__main__':
    param_filename=sys.argv[1]
    param_topic=sys.argv[2]
    checker = WikiCrawler.Checker(filename=param_filename)
    checker.checkReqPackage()
    checker.checkFilePath()
    
