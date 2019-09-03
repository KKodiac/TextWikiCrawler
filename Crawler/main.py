import WikiCrawler
import argparse
import sys


if __name__ == '__main__':
    param_topic=sys.argv[1]
    fname = param_topic+".json"
    checker = WikiCrawler.Checker(filename=fname)
    checker.checkReqPackage()
    checker.checkFilePath()
    
    crawler = WikiCrawler.Crawler(param_topic)
    crawler.requestForHTML()
    # crawler.findLink2NextTopic()

    parser = WikiCrawler.Parser(param_topic)
    parser.returnData()