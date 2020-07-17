'''
@Description: 
@Author: zhu733756
@Date: 2020-07-16 16:53:18
@LastEditTime: 2020-07-17 17:42:40
@LastEditors: zhu733756
'''
# -*- coding: utf-8 -*-
import os
BOT_NAME = 'hot_rank'

SPIDER_MODULES = ['spiders']
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs', '{}.log'.format(BOT_NAME))
LOG_LEVEL = 'WARNING'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

ROBOTSTXT_OBEY = False
# DOWNLOAD_DELAY = 3
# TELNETCONSOLE_ENABLED = False

EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

DOWNLOADER_MIDDLEWARES = {
    'middlewares.UserAgentMiddleware': 543,
}
