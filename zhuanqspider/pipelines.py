# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from settings import IP_POOL

class ZhuanqPipeline(object):
    def process_item(self, item, spider):
        return item
