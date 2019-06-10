# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 15:21
# @Author  : 2simple
# @Site    : Get the recruitment information on the official website of hefei college
# @File    : Recruitment.py
# @Software: PyCharm
from scrapy.spiders import Spider, Request
from classwork.items import hfuuJobItem
import time


class GetJOb(Spider):
    name = 'getJob'
    allowed_domains = ["http://hfuu.good-edu.cn"]
    start_urls = ["http://hfuu.good-edu.cn/showmore.php?actiontype=0&pg=1"]

    def parse(self, response):
        x = len(response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr'))
        for i in range(2, x + 1):
            Item = hfuuJobItem()

            Item['id'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[1]/text()'.format(i)).extract()[0]

            Item['title'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[2]/a/text()'.format(i)).extract()[0].strip()

            Item['pageview'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[3]/text()'.format(i)).extract()[0]

            Item['releaseTime'] = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[4]/text()'.format(i)).extract()[0]

            relative = \
            response.xpath('//*[@id="p2_c"]/div[3]/div[2]/table/tr[{}]/td[2]/a/@href'.format(i)).extract()[0]
            Item['url'] = 'http://hfuu.good-edu.cn/' + relative

            yield Item

        if response.xpath('//*[@id="p2_c"]/div[4]/a[9]/@href'):
            time.sleep(10)
            relativePageUrl = response.xpath('//*[@id="p2_c"]/div[4]/a[9]/@href').extract()[0]
            absolutePageUrl = response.urljoin(relativePageUrl)
            print('absolutePageUrl：' + absolutePageUrl)
            yield Request(url=absolutePageUrl, callback=self.parse, dont_filter=True)
        else:
            print('Work is done')




