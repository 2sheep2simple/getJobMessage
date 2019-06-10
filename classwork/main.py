# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 13:40
# @Author  : 2simple
# @Site    : main function
# @File    : main.py
# @Software: PyCharm

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.abspath(__file__))
execute(['scrapy', 'crawl', 'getJob'])