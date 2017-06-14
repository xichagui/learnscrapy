# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import Request

from zhuanqspider.spiders.spiders_settings import baidu_settings


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://y.baidu.com/song/212835']

    #自定义设置 覆盖settings文件 作用范围为spider
    custom_settings = baidu_settings.custom_settings

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url=url, callback=self.parse, dont_filter=True)
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        print((response.body).decode('utf-8'))
        time.sleep(3)
