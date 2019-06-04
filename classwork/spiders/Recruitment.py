# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 15:21
# @Author  : 2simple
# @Site    : getJobMessage
# @File    : Recruitment.py
# @Software: PyCharm
from scrapy.spiders import Spider, Request
from classwork.items import hfuuJobItem
import time


class GetJOb(Spider):
    name = 'getJob'
    allowed_domains = [""]
    start_urls = [""]

    def parse(self, response):
        x = len(response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr'))
        for i in range(2, x):
            Item = hfuuJobItem()

            Item['id'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[1]/text()'.format(i)).extract()[0]

            Item['title'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[2]/a/text()'.format(i)).extract()[0]

            Item['pageview'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[3]/text()'.format(i)).extract()[0]

            Item['releaseTime'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[4]/text()'.format(i)).extract()[0]

            relative = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[2]/a/@href'.format(i)).extract()[0]
            Item['url'] = '' + relative
            print(Item['url'])
            yield Item

        if response.xpath('//*[@id="p2_c"]/div[4]/a[9]/@href'):
            time.sleep(30)
            relativePageUrl = response.xpath('//*[@id="p2_c"]/div[4]/a[9]/@href').extract()[0]
            absolutePageUrl = response.urljoin(relativePageUrl)
            print('absolutePageUrl：' + absolutePageUrl)
            yield Request(url=absolutePageUrl, callback=self.parse, dont_filter=True)
        else:
            print('Work is done')




