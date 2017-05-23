# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    allowed_domains = ["bilibili.com"]
    start_urls = ['http://space.bilibili.com/322052/']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            # 提供给request代理支持
            'zhuanqspider.middlewares.RandomUserAgent': 100,
        },
    }

    def parse(self, response):
        print(response.url)
