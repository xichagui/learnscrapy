# -*- coding: utf-8 -*-
import json

import re

import logging
import scrapy
import time
from scrapy import FormRequest

from zhuanqspider.items import BilibiliItem
from zhuanqspider.spiders.spiders_settings import bilibili_settings
from zhuanqspider.util.spider_util import SpiderUtil


class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    allowed_domains = ["bilibili.com"]
    start_urls = [
        'http://space.bilibili.com/155616/',
        # 'http://www.bilibili.com/widget/getPageList?aid=51852'
    ]

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         # 提供给request代理支持
    #         'zhuanqspider.middlewares.RandomUserAgent': 100,
    #     },
    # }

    # 自定义设置 覆盖settings文件 作用范围为spider
    custom_settings = bilibili_settings.custom_settings

    mapping_Bilibili = {
        'mid': 'bilibili_mid',
        'name': 'bilibili_name',
        'sex': 'bilibili_sex',
        'face': 'bilibili_img',
        'birthday': 'bilibili_birthday',
        'sign': 'bilibili_sign',
        'fans': 'bilibili_fans',
        'playNum': 'bilibili_play'
    }

    video_item = ['title', 'play', 'description', 'author', 'aid', 'favorites', 'length', 'typeid', 'comment']

    def parse(self, response):
        mid = (re.findall('http://space\.bilibili\.com/(\d{1,10})/', response.url))[0]

        item = BilibiliItem()
        item['bilibili_url'] = response.url

        yield FormRequest(
            'http://space.bilibili.com/ajax/member/GetInfo',
            method='POST',
            formdata={
                'mid': mid,
                'csrf': ''
            },
            meta={'mid': mid, 'item': item},
            callback=self.parse_info,
        )

    def parse_info(self, response):
        json_personal = json.loads(response.body.decode())

        dict_ajax = json_personal['data']

        item = response.meta['item']
        for key, value in self.mapping_Bilibili.items():
            item[value] = dict_ajax[key]

        item['bilibili_regtime'] = time.strftime("%Y-%m-%d", time.localtime(dict_ajax['regtime']))

        _time = str(time.time() * 1000)[:13]
        # http://space.bilibili.com/ajax/settings/getNotice?mid=155616&_=1495866528618
        yield FormRequest(
            'http://space.bilibili.com/ajax/settings/getNotice',
            headers={"Referer": item['bilibili_url']},
            method='GET',
            formdata={
                'mid': item['bilibili_mid'],
                '_': _time
            },
            meta={'item': item},
            callback=self.parse_notice
        )

    def parse_notice(self, response):
        json_object = json.loads(response.body.decode())
        notice = json_object['data']['notice']
        item = response.meta['item']

        if notice:
            item['bilibili_notice'] = notice

        _time = str(time.time() * 1000)[:13]

        yield FormRequest(
            'http://space.bilibili.com/ajax/member/getSubmitVideos',
            headers={"Referer": item['bilibili_url']},
            method='GET',
            formdata={
                'mid': item['bilibili_mid'],
                'pagesize': '30',
                'page': '1',
                'keyword': '',
                'order': 'senddate',
                '_': _time
            },
            meta={'page': 1, 'item': item},
            callback=self.parse_submit_videos
        )

    def parse_submit_videos(self, response):
        json_object = json.loads(response.body.decode())
        item = response.meta['item']
        page = response.meta['page']

        if page < json_object['data']['pages']:
            _time = str(time.time() * 1000)[:13]
            page += 1

            yield FormRequest(
                'http://space.bilibili.com/ajax/member/getSubmitVideos',
                headers={"Referer": item['bilibili_url']},
                method='GET',
                formdata={
                    'mid': item['bilibili_mid'],
                    'pagesize': '30',
                    'page': str(page),
                    'keyword': '',
                    'order': 'senddate',
                    '_': _time
                },
                meta={'page': page, 'item': item},
                callback=self.parse_submit_videos
            )

        vlist = json_object['data']['vlist']
        for v in vlist:
            item2 = BilibiliItem(item)  # 复制item
            # 视频基本信息
            for k in self.video_item:
                item2[k] = v[k]

            item['created'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(v['created']))
            item2['video_url'] = 'http://www.bilibili.com/video/av' + str(v['aid']) + '/'
            item2['pic'] = 'http:' + v['pic']

            yield FormRequest(
                'http://api.bilibili.com/archive_stat/stat',
                headers={"Referer": item2['bilibili_url']},
                method='GET',
                formdata={
                    'callback': SpiderUtil.get_random_callback_name(),
                    'aid': str(item2['aid']),
                    'type': 'jsonp',
                    'order': 'senddate',
                    '_': str(time.time() * 1000)[:13]
                },
                meta={'item': item2},
                callback=self.parse_video_coin
            )

    def parse_video_coin(self, response):
        item = response.meta['item']
        # 视频硬币数
        m = re.search('^jQuery[0-9_]*\((.*)\);$', response.body_as_unicode())
        json_dict = json.loads(m.group(1))

        item['coin'] = json_dict['data']['coin']

        yield FormRequest(
            'http://api.bilibili.com/x/tag/archive/tags',
            headers={"Referer": item['bilibili_url']},
            method='GET',
            formdata={
                'callback': SpiderUtil.get_random_callback_name('bilibili'),
                'aid': str(item['aid']),
                'jsonp': 'jsonp',
                '_': str(time.time() * 1000)[:13]
            },
            meta={'item': item},
            callback=self.parse_video_tags
        )

    def parse_video_tags(self, response):
        item = response.meta['item']
        # 视频标签
        m = re.search('^jQuery[0-9_]*\((.*)\)$', response.body_as_unicode())
        json_dict = json.loads(m.group(1))

        # 可能会没有标签
        if json_dict['code'] == 0:
            tag = []
            try:
                for v in json_dict['data']:
                    tag.append(v['tag_name'])
                item['tags'] = tag
            except:
                logging.debug('没有标签')
        else:
            logging.debug(json_dict['code'], response.url)

        yield FormRequest(
            'http://www.bilibili.com/widget/getPageList',
            headers={"Referer": item['bilibili_url']},
            method='GET',
            formdata={
                'aid': str(item['aid']),
            },
            meta={'item': item},
            callback=self.parse_video_list
        )

    def parse_video_list(self, response):
        # 多p视频
        json_object = json.loads(response.body_as_unicode())

        item = response.meta['item']

        if len(json_object) > 1:
            video_list = []
            for v in json_object:
                video = {}
                video['title'] = v['pagename']
                video['video_url'] = item['video_url'] + 'index_' + str(v['page']) + '.html'
                video_list.append(video)
            item['video_list'] = video_list

        yield item
