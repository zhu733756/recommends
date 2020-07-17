'''
@Description: 
@Author: zhu733756
@Date: 2020-07-17 17:28:01
@LastEditTime: 2020-07-17 17:28:36
@LastEditors: zhu733756
'''
import scrapy


class HotRankItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    search_num = scrapy.Field()
    rank = scrapy.Field()
    tags = scrapy.Field()
    create_date = scrapy.Field()
