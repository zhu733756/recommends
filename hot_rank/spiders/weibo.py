'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 16:53:18
@LastEditTime: 2020-07-17 17:29:13
@LastEditors: zhu733756
'''
# -*- coding: utf-8 -*-
import json
import scrapy
from datetime import datetime
from urllib.parse import unquote
from . import HotRankItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = [
        'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6']
    rank_type = 'weibo'

    def parse(self, response):
        tr_list = response.xpath(
            "//div[@id='pl_top_realtimehot']/table/tbody/tr")
        for tr in tr_list:
            item = HotRankItem()
            item['title'] = tr.xpath(
                "./td[@class='td-02']/a/text()").extract_first('')
            url = response.urljoin(
                tr.xpath("./td[@class='td-02']/a/@href").extract_first(''))
            url2 = response.urljoin(
                tr.xpath("./td[@class='td-02']/a/@href_to").extract_first(''))
            item['url'] = url2 if 'javascript:void' in url else url
            item['type'] = self.rank_type
            item['search_num'] = tr.xpath(
                "./td[@class='td-02']/span/text()").extract_first('')
            item['rank'] = tr.xpath(
                "./td[contains(@class, 'td-01')]/text()").extract_first('0')
            item['tags'] = tr.xpath(
                "./td[@class='td-03']/i[contains(@class, 'icon-txt')]/text()").extract_first('')
            item['create_date'] = str(datetime.now())
            yield item
