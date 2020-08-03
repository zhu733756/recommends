'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 17:44:13
@LastEditTime: 2020-08-03 14:41:35
@LastEditors: zhu733756
'''
import sys
import json
import os

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.baidu import BaiduSpider
from spiders.sogouweixin import SogouweixinSpider
from spiders.weibo import WeiboSpider

from scrapy.signalmanager import dispatcher

spider_map = {
    "baidu": BaiduSpider,
    "weixin": SogouweixinSpider,
    "weibo": WeiboSpider
}

os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'settings')


def spider_results(spidername):
    spider_class = None
    if spidername not in spider_map:
        return []

    spider_class = spider_map[spidername]
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(dict(item))

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    process = CrawlerProcess(get_project_settings())
    # spider_class可以是爬虫文件中name中的字符串, 也可以是import导入的类
    process.crawl(spider_class)
    process.start()  # the script will block here until the crawling is finished
    return results


if __name__ == '__main__':
    spidername = 'baidu' if len(sys.argv) <= 1 else sys.argv[1]
    searchresult = spider_results(spidername)
    print(searchresult)
