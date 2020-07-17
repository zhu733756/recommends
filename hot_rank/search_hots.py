'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 17:44:13
@LastEditTime: 2020-07-17 17:27:51
@LastEditors: zhu733756
'''
import sys
import json

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.baidu import BaiduSpider
from spiders.sogouweixin import SogouweixinSpider
from spiders.weibo import WeiboSpider

from scrapy.signalmanager import dispatcher


def spider_results(spidername):
    spider_class = None
    if spidername == "baidu":
        spider_class = BaiduSpider
    elif spidername == "weixin":
        spider_class = SogouweixinSpider
    elif spidername == "weibo":
        spider_class = WeiboSpider
    else:
        return []

    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(dict(item))

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_class)
    process.start()  # the script will block here until the crawling is finished
    return json.dumps(results, ensure_ascii=False).encode('gbk', 'ignore').decode('gbk')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        spidername = sys.argv[1]
        searchresult = spider_results(spidername)
        print(searchresult)
