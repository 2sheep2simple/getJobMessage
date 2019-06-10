# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors


class ClassworkPipeline(object):
    def __init__(self):
        try:
            self.connect = pymysql.connect(
                host='124.156.118.28',
                port=3306,
                database='scrapy',
                user='scrapy',
                passwd='Heyyyy@1996',
                charset='utf8'
            )
        except Exception:
            print('connect error')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            sql = 'INSERT INTO jobmessage(id, title, pageview, releaseTime, url) VALUES ("%s", "%s", "%s", "%s", "%s")' % (
                item['id'], item['title'], item['pageview'], item['releaseTime'], item['url'])
            self.cursor.execute(sql)
            self.connect.commit()
            return item
        except Exception:
            self.connect.rollback()
