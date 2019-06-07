from scrapy.crawler import CrawlerProcess

from data import Data

from login import Login

if __name__ == '__main__':
    process = CrawlerProcess()

    process.crawl(Login)

    process.crawl(Data)
    
    process.start()