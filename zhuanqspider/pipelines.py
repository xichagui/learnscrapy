# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymongo


class ZhuanqPipeline(object):
    def process_item(self, item, spider):
        return item


class Kugou5singPl(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        # self.file = open('items.jl', 'w')
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGODB_URI'),
            mongo_db = crawler.settings.get('MONGODB_DB'),
            mongo_collection = crawler.settings.get('MONGODB_COLLECTION_PROXY')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db[self.mongo_collection].insert(dict(item))
        except:
            logging.info('insert error')
        return item


