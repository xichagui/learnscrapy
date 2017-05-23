# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KugouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #个人信息
    kugou_name = scrapy.Field()
    kugou_fans = scrapy.Field()
    kugou_popular = scrapy.Field()
    kugou_img = scrapy.Field()
    kugou_sign = scrapy.Field()
    kugou_url = scrapy.Field()


    #歌曲信息
    song_name = scrapy.Field()
    singer = scrapy.Field()
    lyricist = scrapy.Field()
    composer = scrapy.Field()
    arrange = scrapy.Field()
    mixer = scrapy.Field()
    type = scrapy.Field()
    language = scrapy.Field()
    style = scrapy.Field()
    download = scrapy.Field()
    upload_time = scrapy.Field()
    original_singer = scrapy.Field()
    song_popular = scrapy.Field()
    song_click = scrapy.Field()
    song_download_count = scrapy.Field()
    song_collect = scrapy.Field()
    song_like = scrapy.Field()
