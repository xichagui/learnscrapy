# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request, FormRequest

from zhuanqspider.items import BaiduItem
from zhuanqspider.spiders.spiders_settings import baidu_settings


class Music163Spider(scrapy.Spider):
    name = "music163"
    allowed_domains = ["163.com"]
    start_urls = [
        'http://music.163.com/artist?id=10089',
        # 'http://music.163.com/artist/album?id=10089',
        # 'http://music.163.com/artist/mv?id=10089',
    ]

    SONG_MAPPING = {
        '演唱': 'singer',
        '作词': 'lyricist',
        '作曲': 'composer',
        '编曲': 'arrange',
        '混编': 'mixer',
        '发行': 'upload_time'
    }

    # 自定义设置 覆盖settings文件 作用范围为spider
    # custom_settings = baidu_settings.custom_settings

    def start_requests(self):
        for url in self.start_urls:
            request = Request(
                url=url,
                headers={'Referer': 'http://music.163.com/'},
                callback=self.parse,
                dont_filter=True,
            )
            yield request

    def parse(self, response):
        url = response.url
        id = re.search('id=(\d{1,10})',url).group(1)
        user_url = response.urljoin(response.xpath('//a[@id="artist-home"]/@href').extract()[0])
        name = response.xpath('//h2[@id="artist-name"]/text()').extract()[0]
        img = response.xpath('//div[@class="n-artist f-cb"]/img/@src').extract()[0]
        alias_str = response.xpath('//h3[@id="artist-alias"]/text()').extract()[0]
        alias = alias_str.replace('\n', '').split(';')

        yield FormRequest(
            url=user_url,
            headers={'Referer': 'http://music.163.com/'},
            callback=self.parse_user,
        )

        # try:
        #     print(response.xpath('//ul[contains(@class, "m-cvrlst")]').extract()[0])
        # except:
        #     pass

    def parse_user(self, response):
        item = response.meta['item']

        ava = response.xpath('//*[@id="ava"]//img/@src').extract()[0]
        name = response.xpath('//*[contains(@class, "name")]//span[contains(@class, "tit")]/text()').extract()[0]
        fans = response.xpath().extract()[0]

        yield FormRequest(
            url='',
            headers={'Referer': 'http://music.163.com/'},
            callback=self.parse_ablum,
        )

    def parse_ablum(self, response):
        pass

