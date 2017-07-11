# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request

from zhuanqspider.items import BaiduItem
from zhuanqspider.spiders.spiders_settings import baidu_settings


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        'http://y.baidu.com/zhengbanhetu',
        # 'http://y.baidu.com/xiaoyiqing',
        'http://y.baidu.com/song/327326',
    ]

    SONG_MAPPING = {
        '演唱': 'singer',
        '作词': 'lyricist',
        '作曲': 'composer',
        '编曲': 'arrange',
        '混编': 'mixer',
        '发行': 'upload_time',
    }

    # 自定义设置 覆盖settings文件 作用范围为spider
    custom_settings = baidu_settings.custom_settings

    def start_requests(self):
        # for url in self.start_urls:
        #     request = Request(url=url, callback=self.parse, dont_filter=True)
        #     request.meta['PhantomJS'] = True
        #     yield request
        request = Request(
            url='http://y.baidu.com/song/327326',
            callback=self.parse_song,
            dont_filter=True,
            meta={
                'item': BaiduItem(),
                'PhantomJS': True,
            }
        )
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
                callback=self.parse_song,
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

    def parse_song(self, response):
        item = response.meta['item']

        item['title'] = response.css('#song_title::text').extract()[0]
        base_info_list = response.css('.base-info .bd li::text').extract()
        for info in base_info_list:
            _info = info.split('：')
            item[self.SONG_MAPPING[_info[0]]] = _info[1]

        inspiration_div = response.css('.song-story .bd').extract()[0]
        inspiration_m = re.search('<div class="bd">([\s\S]*)</div>', inspiration_div)
        item['inspiration'] = inspiration_m.group(1)
        lrc_div = response.css('.song-lrc #lyric-content').extract()[0]
        item['lrc'] = re.search('<div id="lyric-content" class="lyric-hidden">([\s\S]*)</div>', lrc_div).group(1)

        play_str = response.css('.listen-times span::text').extract()[0]

        if '万' in play_str:
            item['play'] = str(int(float(play_str[:-1]) * 10000))
        else:
            item['play'] = play_str

        yield item
