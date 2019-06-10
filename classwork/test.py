# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 10:23
# @Author  : 2simple
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pymysql

try:
    connect = pymysql.connect(
        host='124.156.118.28',
        port=3306,
        database='scrapy',
        user='root',
        passwd='Heyyyy@1996',
        charset='utf8'
    )
    cursor = connect.cursor()
    sql = 'INSERT INTO message(id, title, pageview, releaseTime, url) VALUES ("%s", "%s", "%s", "%s", "%s")' % (
        '2', '安徽', '99', '2019-0-0',
        'www.baidu.com')
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
except Exception:
    print('connect error')



