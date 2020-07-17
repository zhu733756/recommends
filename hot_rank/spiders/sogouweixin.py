'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 17:01:06
@LastEditTime: 2020-07-17 17:47:41
@LastEditors: zhu733756
'''
# -*- coding: utf-8 -*-
import json
import scrapy
from datetime import datetime
from urllib.parse import unquote
from . import HotRankItem


class SogouweixinSpider(scrapy.Spider):
    name = 'sogouweixin'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['https://weixin.sogou.com/']
    rank_type = 'weixin'

    def parse(self, response):
        tr_list = response.xpath(
            "//div[@class='snb-right']/div[@class='aside']//li")
        for tr in tr_list:
            item = HotRankItem()
            item['title'] = tr.xpath("./a/text()").extract_first('')
            url = response.urljoin(
                tr.xpath("./a/@href").extract_first(''))
            item['url'] = url
            item['type'] = self.rank_type
            item['search_num'] = ''
            item['rank'] = tr.xpath(
                "./i/text()").extract_first('')
            item['tags'] = ''
            item['create_date'] = str(datetime.now())
            yield item
