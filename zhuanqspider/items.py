# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KugouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kugou_name = scrapy.Field()
    kugou_fans = scrapy.Field()
    kugou_popular = scrapy.Field()
    kugou_img = scrapy.Field()
    kugou_sign = scrapy.Field()
