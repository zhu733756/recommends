'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 16:53:18
@LastEditTime: 2020-07-17 17:46:05
@LastEditors: zhu733756
'''
# -*- coding: utf-8 -*-
import json
import scrapy
from datetime import datetime
from urllib.parse import unquote
from . import HotRankItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']
    rank_type = 'baidu'
    hotTags = {
        '0': '',
        '1': '新',
        '2': '荐',
        '3': '热',
        '4': '沸',
        '5': '爆',
    }

    def parse(self, response):
        hotsearch_data = response.xpath(
            '//textarea[@id="hotsearch_data"]/text()').extract_first('')
        data = json.loads(hotsearch_data)
        hotsearch = data.get('hotsearch')
        for index, i in enumerate(hotsearch):
            item = HotRankItem()
            item['title'] = i.get('pure_title')
            item['url'] = unquote(i.get('linkurl', ''))
            item['type'] = self.rank_type
            item['search_num'] = i.get('heat_score')
            item['rank'] = index + 1
            hotTags = i.get('hotTags')
            item['tags'] = self.hotTags.get(hotTags, '')
            item['create_date'] = str(datetime.now())
            yield item
