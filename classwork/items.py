# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class hfuuJobItem(scrapy.Item):
    # 序号
    id = Field()
    # 标题
    title = Field()
    # 阅读数
    pageview = Field()
    # 发布时间
    releaseTime = Field()
    # 文章链接
    url = Field()

