# -*- coding: utf-8 -*-
import logging
import scrapy


class Kugou5singSpider(scrapy.Spider):
    name = "kugou_5sing"
    allowed_domains = ["kugou.com"]
    start_urls = ['http://5sing.kugou.com/tenderjun/default.html',
                  'http://5sing.kugou.com/tenderjun/default.html',
                  'http://5sing.kugou.com/',
                  ]

    def parse(self, response):
        logging.info('status code is %d', response.status)
