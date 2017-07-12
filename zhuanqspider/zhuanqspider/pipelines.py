# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

# import pymongo
import scrapy

import spiderapp
from spiderapp.models import Author, Work, Style
from zhuanqspider.items import KugouUserItem, KugouItem


class ZhuanqPipeline(object):
    def process_item(self, item, spider):
        return item

class Kugou5singPl(object):

    def process_item(self, item, spider):
        if isinstance(item, KugouUserItem):
            print('作者')
            try:
                author = Author.objects.get(kugou_url=item['kugou_url'])
            except:
                author = Author(name=item['name'], kugou_url=item['kugou_url'])

            author.fans = item['fans']
            author.popular = item['popular']
            author.head_url = item['img']
            try:
                author.sign = item['sign']
            except:
                pass

            # author.kugou_is_vip = item['is_vip']
            # author.kugou_is_realname = item['is_realname']
            # author.kugou_is_tao = item['is_tao']
            # author.kugou_is_musician = item['is_musician']
            # author.kugou_is_liver = item['is_liver']
            # author.kugou_is_recommend = item['is_recommend']
            # author.kugou_is_star = item['is_star']
            # author.kugou_is_mobile = item['is_mobile']
            # author.kugou_is_xinlang = item['is_xinlang']
            # author.kugou_is_renren = item['is_renren']
            # author.kugou_is_tengxun = item['is_tengxun']

            author.save()
        elif isinstance(item, KugouItem):
            # work = Work(title=item['song_name'])
            singer = Author.objects.get_or_create(name=item['singer']) if item['singer'] else None
            lyricist = Author.objects.get_or_create(name=item['lyricist']) if item['lyricist'] else None
            composer = Author.objects.get_or_create(name=item['composer']) if item['composer'] else None
            arrange = Author.objects.get_or_create(name=item['arrange']) if item['arrange'] else None
            mixer = Author.objects.get_or_create(name=item['mixer']) if item['mixer'] else None
            # original_singer = Author.objects.get_or_create(name=item['original_singer']) if item[
            #     'original_singer'] else None

            style_list = []
            if item['style']:
                for s in item['style']:
                    style = Style.objects.get_or_create(name=s)
                    style_list.append(style)


            w = Work(title=item['song_name'], language=item['language'], upload_time=item['upload_time'],
                     lrc=item['lrc'], inspiration=item['inspiration'], popular=item['song_popular'],
                     click=item['song_click'], download_count=item['song_download_count'],
                     collect=item['song_collect'], like=item['song_like'], kugou_url=item['song_url']
                     )
            w.save()

            if singer:
                w.singer.add(singer[0])

            if lyricist:
                w.lyricist.add(lyricist[0])

            if composer:
                w.composer.add(composer[0])

            if arrange:
                w.arrange.add(arrange[0])

            if mixer:
                w.mixer.add(mixer[0])

            # if original_singer:
            #     w.singer.add(original_singer[0])

            for s in style_list:
                w.style.add(s[0])

        return item


class BilibiliPl(object):

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
            mongo_collection = crawler.settings.get('MONGODB_COLLECTION_BILIBILI')
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


