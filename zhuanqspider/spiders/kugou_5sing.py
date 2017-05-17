# -*- coding: utf-8 -*-
import logging

import re
import scrapy
from scrapy import Request

from items import KugouItem


class Kugou5singSpider(scrapy.Spider):


    name = "kugou_5sing"
    allowed_domains = ["kugou.com"]
    start_urls = [
                    'http://5sing.kugou.com/muhan/default.html',
                    # 'http://5sing.kugou.com/crazyman/default.html',
                    # 'http://5sing.kugou.com/inory/default.html',
                    # 'http://5sing.kugou.com/jarellee/default.html',
                    # 'http://5sing.kugou.com/462455/default.html',
                    # 'http://5sing.kugou.com/muhan/yc/1.html',
                  ]

    # per_spider配置, 将覆盖settings设置
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
           # 提供给request代理支持
           'zhuanqspider.middlewares.RandomUserAgent': 100,
        },
        # 'ROBOTSTXT_OBEY' : False
    }

    def parse(self, response):
        logging.info('%s status code is %d' % (response.url, response.status))
        title = response.selector.xpath('/html/head/title/text()').extract()
        item = KugouItem()

        html_text = str(response.body, encoding="utf-8")
        '''
            <script type="text/javascript">
                var OwnerNickName = '「M」Crazyman狮子';
        '''
        item['kugou_name'] = re.search('var OwnerNickName = \'(.*)\'', html_text).group(1)
        item['kugou_popular'] = re.search('\d+', response.selector.xpath('//*[@id="totalrq"]/a/text()').extract()[0]).group(0)
        item['kugou_fans'] =  re.search('\d+', response.selector.xpath('//*[@id="totalfans"]/a/text()').extract()[0]).group(0)

        #针对目前发现的5种 5sing主页
        img, version = self.getImgAndVersion(response)
        item['kugou_img'] = img

        song_url_list = []
        song_url_list.append(response.urljoin('yc/1.html'))
        song_url_list.append(response.urljoin('fc/1.html'))
        song_url_list.append(response.urljoin('bz/1.html'))

        for url in song_url_list:
            yield Request(url, callback=self.parse_lists, meta={'item': item})

    def parse_lists(self, response):
        #分析原创、翻唱、伴奏页面，提取当前页歌曲连接以及下一页
        logging.info('%s status code is %d' % (response.url, response.status))
        item = response.meta['item']
        html_text = str(response.body, encoding="utf-8")
        song_list = response.selector.css('li strong a::attr(href)').extract()

        for url_path in song_list:
            # yield Request(url_path, callback=self.parse_song, meta={'item': item})
            print(url_path)

        try:
            m = re.search('<a class=\"noFlush_load_link\".*href=\"(.*)\".*下一页</a>', html_text)
            next_page_url = response.urljoin(m.group(1))
            yield Request(next_page_url, callback=self.parse_lists, meta={'item': item})
            #yield Request('http://5sing.kugou.com/muhan/yc/2.html', callback=self.parse_lists, meta={'item': item})
        except Exception:
            print('没有下一页了')

    def parse_song(self, response):
        print('parse_song_url:-----', response.url)

    def getImgAndVersion(self, response):
        kugou_img = ''
        version = 0
        if len(response.selector.css('.user_pic img::attr(src)').extract()) > 0:
            version = 1
            kugou_img = response.selector.css('.user_pic img::attr(src)').extract()[0]
        elif len(response.selector.css('.photo img::attr(src)').extract()) > 0:
            version = 2
            kugou_img = response.selector.css('.photo img::attr(src)').extract()[0]
        elif len(response.selector.css('.my_pic img::attr(src)').extract()) > 0:
            version = 3
            kugou_img = response.selector.css('.my_pic img::attr(src)').extract()[0]
        elif len(response.selector.css('.m_about img::attr(src)').extract()) > 0:
            version = 4
            kugou_img = response.selector.css('.m_about img::attr(src)').extract()[0]
        elif len(response.selector.css('.b_con span img::attr(src)').extract()) > 0:
            version = 5
            kugou_img = response.selector.css('.b_con span img::attr(src)').extract()[0][:-12] + '_180_180.jpg'

        return kugou_img, version

    def start_requests(self):
        return [Request("http://www.baidu.com", callback=self.logged_in)]

    def logged_in(self, response):
        print(response.url)





