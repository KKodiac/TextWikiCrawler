import WikiCrawler
import argparse
import sys


if __name__ == '__main__':
    param_topic=sys.argv[1]
    parser = WikiCrawler.Parser(param_topic)
    parser.checkRequirements()
    parser.returnData()
    parser.addToSQL()