import WikiCrawler
import argparse
import sys

if __name__ == '__main__':
    param_filename=sys.argv[1]
    checker = WikiCrawler.Checker(filename=param_filename)
    checker.checkReqPackage()

    
