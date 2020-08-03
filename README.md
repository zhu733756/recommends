## 基于采集的热点推荐

#### 基本原理

通过搜索百度、微博、微信热点分词分别与数据库中的网站、电子报、微博、微信采集数据进行标题、内容比对，生成热点文章进行推荐。

#### 采集部分

- hot_rank
    - items
        -  `spiders/__init__.py`

- 运行入口
    - `python search_host.py  baidu/weixin/weibo【三选一】`

#### 分词部分

- es
    

- todo
    - 安装ik分词器
    - 知乎爬虫

