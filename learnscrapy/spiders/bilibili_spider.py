# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpiderSpider(scrapy.Spider):
    name = "bilibili_spider"
    allowed_domains = ["bilibili.com"]
    start_urls = ['http://bilibili.com/']

    def parse(self, response):
        pass
