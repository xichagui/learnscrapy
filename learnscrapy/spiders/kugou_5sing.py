# -*- coding: utf-8 -*-
import scrapy


class Kugou5singSpider(scrapy.Spider):
    name = "kugou_5sing"
    allowed_domains = ["kugou.com"]
    start_urls = ['http://kugou.com/']

    def parse(self, response):
        pass
