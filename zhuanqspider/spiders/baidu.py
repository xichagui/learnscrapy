# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import Request, FormRequest

from zhuanqspider.items import BaiduItem
from zhuanqspider.spiders.spiders_settings import baidu_settings


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        'http://y.baidu.com/zhengbanhetu',
        # 'http://y.baidu.com/xiaoyiqing',
    ]

    # 自定义设置 覆盖settings文件 作用范围为spider
    custom_settings = baidu_settings.custom_settings

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url=url, callback=self.parse, dont_filter=True)
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        # html = (response.body).decode('utf-8')

        item = BaiduItem()
        item['baidu_name'] = response.css('.artist-name a::text').extract()[0]
        item['baidu_url'] = response.url
        try:
            item['baidu_notice'] = response.css(
                '.content::attr(data-content)').extract()[0]
        except IndexError:
            pass
        artist_data = response.css('.artist-data strong::text').extract()
        item['baidu_fans'] = artist_data[0]
        item['baidu_songs'] = artist_data[1]
        item['baidu_listen'] = artist_data[2]
        artist_data2 = response.css('.style')
        item['baidu_style'] = artist_data2[0].css('a::text').extract()[0]

        baidu_type_str = artist_data2[1].css('.more::text').extract()[0]
        baidu_type = baidu_type_str.split(',')
        item['baidu_type'] = baidu_type

        songlist_url = response.css('.nav-main li a::attr(href)').extract()[1]

        yield Request(
            response.urljoin(songlist_url),
            callback=self.parse_song_list,
            meta={'PhantomJS': True, 'item': item}
        )

    def parse_song_list(self, response):
        item = response.meta['item']

        song_urls = response.css('.widget li .title a::attr(href)').extract()
        for url in song_urls:
            yield Request(
                response.urljoin(url),
                callback=self.song_parse,
                meta={'PhantomJS': True, 'item': item}
            )

        try:
            next_url = response.css('.page-link.next::attr(href)').extract()[0]

            yield Request(
                response.urljoin(next_url),
                callback=self.parse_song_list,
                meta={'PhantomJS': True, 'item': item}
            )
        except IndexError:
            pass

    def song_parse(self, response):
        print(response.url)
        # pass