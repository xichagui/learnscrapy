# -*- coding: utf-8 -*-
import base64
import json
import logging

import re
import time
from scrapy import Request, FormRequest
from scrapy.spiders import CrawlSpider


from zhuanqspider.items import KugouItem, KugouUserItem
from .spiders_settings import kugou_5sing_settings
from zhuanqspider.util.spider_util import SpiderUtil


class Kugou5singSpider(CrawlSpider):
    name = "kugou_5sing"
    allowed_domains = ["kugou.com"]

    start_urls=[
        # 'http://5sing.kugou.com/462455/default.html',
        # 'http://5sing.kugou.com/6339738/default.html',
        # 'http://5sing.kugou.com/676529/default.html',
        # 'http://5sing.kugou.com/676550/default.html',
        # 'http://5sing.kugou.com/zhucool/default.html',
        # 'http://5sing.kugou.com/crazyman/default.html',
        # 'http://5sing.kugou.com/jarellee/default.html',
        # 'http://5sing.kugou.com/sibyliest/default.html',
        # 'http://5sing.kugou.com/ryutsuki/default.html',
        # 'http://5sing.kugou.com/qingnong/default.html',
        # 'http://5sing.kugou.com/fairyaki/default.html',
        # 'http://5sing.kugou.com/141092/default.html',
        # 'http://5sing.kugou.com/GaaraEmma/default.html',
        # 'http://5sing.kugou.com/3705892/default.html',
        # 'http://5sing.kugou.com/6536715/default.html',
        # 'http://5sing.kugou.com/zhiyouyingzi/default.html',
        # 'http://5sing.kugou.com/xuduokui/default.html',
        # 'http://5sing.kugou.com/zica2335072748/default.html',
        # 'http://5sing.kugou.com/15139626/default.html',
        # 'http://5sing.kugou.com/17327156/default.html',
        # 'http://5sing.kugou.com/dongli/default.html',
        # 'http://5sing.kugou.com/yuxuanji/default.html',
        # 'http://5sing.kugou.com/1125409/default.html',
        # 'http://5sing.kugou.com/C210491/default.html',
        # 'http://5sing.kugou.com/CcccEs/default.html',
        # 'http://5sing.kugou.com/wuen/default.html',
        # 'http://5sing.kugou.com/lietian/default.html',
        # 'http://5sing.kugou.com/2449235/default.html',
        # 'http://5sing.kugou.com/soul/default.html',
        # 'http://5sing.kugou.com/misiaxiaoyu/default.html',
        # 'http://5sing.kugou.com/9847237/default.html',
        # 'http://5sing.kugou.com/35524722/default.html',
        # 'http://5sing.kugou.com/34698480/default.html',
        # 'http://5sing.kugou.com/lazysnoopy/default.html',
        # 'http://5sing.kugou.com/assen/default.html',
        # 'http://5sing.kugou.com/wuyinjw/default.html',
        # 'http://5sing.kugou.com/30070422/default.html',
        # 'http://5sing.kugou.com/braska/default.html',
        # 'http://5sing.kugou.com/tenderjun/default.html',
        # 'http://5sing.kugou.com/xiaoqu/default.html',
        # 'http://5sing.kugou.com/kaxiu/default.html',
        # 'http://5sing.kugou.com/21769331/default.html',
        # 'http://5sing.kugou.com/8308175/default.html',
        # 'http://5sing.kugou.com/11750769/default.html',
        # 'http://5sing.kugou.com/muhan/default.html',
        # 'http://5sing.kugou.com/qiran/default.html',
        # 'http://5sing.kugou.com/rajor/default.html',
        # 'http://5sing.kugou.com/xiaozhui/default.html',
        # 'http://5sing.kugou.com/wuseshinanye/default.html',
        # 'http://5sing.kugou.com/12292483/default.html',
        # 'http://5sing.kugou.com/qiaokechidao/default.html',
        # 'http://5sing.kugou.com/xiaoyiqing/default.html',
        # 'http://5sing.kugou.com/lgmcc/default.html',
        # 'http://5sing.kugou.com/teman/default.html',
        # 'http://5sing.kugou.com/kazuki/default.html',
        # 'http://5sing.kugou.com/winky/default.html',
        # 'http://5sing.kugou.com/critty/default.html',
        # 'http://5sing.kugou.com/mario/default.html',
        # 'http://5sing.kugou.com/Tacke/default.html',
        # 'http://5sing.kugou.com/weepclouds/default.html',
        # 'http://5sing.kugou.com/yinlin/default.html',
        # 'http://5sing.kugou.com/zhixuan/default.html',
        # 'http://5sing.kugou.com/10789829/default.html',
        # 'http://5sing.kugou.com/3877985/default.html',
        # 'http://5sing.kugou.com/huanger/default.html',
        # 'http://5sing.kugou.com/xuanshang/default.html',
        # 'http://5sing.kugou.com/echien/default.html',
        # 'http://5sing.kugou.com/lingzhixuan/default.html',
        # 'http://5sing.kugou.com/9035866/default.html',
        # 'http://5sing.kugou.com/4803845/default.html',
        # 'http://5sing.kugou.com/midaho/default.html',
        # 'http://5sing.kugou.com/nanfengzjn/default.html',
        # 'http://5sing.kugou.com/shaosiming/default.html',
        # 'http://5sing.kugou.com/kemuqing/default.html',
        # 'http://5sing.kugou.com/XGJUN/default.html',
        # 'http://5sing.kugou.com/9808742/default.html',
        # 'http://5sing.kugou.com/35341590/default.html',
        # 'http://5sing.kugou.com/yousa/default.html',
        # 'http://5sing.kugou.com/inory/default.html',
        # 'http://5sing.kugou.com/daiquan/default.html',
        # 'http://5sing.kugou.com/5632611/default.html',
        # 'http://5sing.kugou.com/paigu/default.html',
        # 'http://5sing.kugou.com/jiangnancheng/default.html',
        # 'http://5sing.kugou.com/7047532/default.html',
        # 'http://5sing.kugou.com/yeluoluo/default.html',
        # 'http://5sing.kugou.com/nekoouka/default.html',
        # 'http://5sing.kugou.com/1923131/default.html',
        # 'http://5sing.kugou.com/33884712/default.html',
        # 'http://5sing.kugou.com/45709658/default.html',
        # 'http://5sing.kugou.com/20232028/default.html',
        # 'http://5sing.kugou.com/dongzi/default.html',
        # 'http://5sing.kugou.com/12634904/default.html',
        # 'http://5sing.kugou.com/929497/default.html',
        # 'http://5sing.kugou.com/yaqing/default.html',
        # 'http://5sing.kugou.com/NLbufen/default.html',
        # 'http://5sing.kugou.com/genxiaoba/default.html',
        # 'http://5sing.kugou.com/1981560/default.html',
        # 'http://5sing.kugou.com/kbshinya/default.html',
        # 'http://5sing.kugou.com/38798531/default.html',
        # 'http://5sing.kugou.com/733942/default.html',
        # 'http://5sing.kugou.com/siqi647/default.html',
        'http://5sing.kugou.com/9286091/default.html',
        'http://5sing.kugou.com/sakuraookami/default.html',
    ]



    # 自定义设置 覆盖settings文件 作用范围为spider
    custom_settings = kugou_5sing_settings.custom_settings

    SONG_MAPPING = {
        '演唱：': 'singer',
        '作词：': 'lyricist',
        '作曲：': 'composer',
        '编曲：': 'arrange',
        '混缩：': 'mixer',
        '分类：': 'type',
        '语种：': 'language',
        '曲风：': 'style',
        '下载设置：': 'download',
        '上传时间：': 'upload_time',
        '原唱：': 'original_singer'}


    def parse(self, response):
        logger = logging.getLogger('kugou_5sing_parse')
        logger.info('%s status code is %d' % (response.url, response.status))
        # item = KugouItem()
        item = KugouUserItem()
        '''
            <script type="text/javascript">
                var OwnerNickName = '「M」Crazyman狮子';
        '''
        # item['kugou_name'] = re.search('var OwnerNickName = \'(.*)\'', response.body_as_unicode()).group(1)
        # item['kugou_url'] = response.url
        # item['kugou_popular'] = re.search('\d+',
        #                                   response.selector.xpath('//*[@id="totalrq"]/a/text()').extract()[0]).group(0)
        # item['kugou_fans'] = re.search('\d+',
        #                                response.selector.xpath('//*[@id="totalfans"]/a/text()').extract()[0]).group(0)
        #
        # # 针对目前发现的5种 5sing主页
        # img, version = self.get_img_a_version(response)
        # item['kugou_img'] = img

        item['name'] = re.search('var OwnerNickName = \'(.*)\'', response.body_as_unicode()).group(1)
        item['kugou_url'] = response.url
        item['popular'] = re.search('\d+',
                                          response.selector.xpath('//*[@id="totalrq"]/a/text()').extract()[0]).group(0)
        item['fans'] = re.search('\d+',
                                       response.selector.xpath('//*[@id="totalfans"]/a/text()').extract()[0]).group(0)

        # 针对目前发现的5种 5sing主页
        img, version = self.get_img_a_version(response)
        item['img'] = img

        # 小图标
        icons = re.findall('static\.5sing\.kugou\.com/images/Special/([^u].*?)\.gif', response.body_as_unicode())
        for icon in icons:
            item['is_' + icon] = True

        song_url_list = list()
        song_url_list.append(response.urljoin('yc/1.html'))
        # song_url_list.append(response.urljoin('fc/1.html'))
        # song_url_list.append(response.urljoin('bz/1.html'))

        yield item

        for url in song_url_list:
            # yield Request(url, callback=self.parse_lists, meta={'item': item, 'version': version})
            yield Request(url, callback=self.parse_lists, meta={'version': version})

    def parse_lists(self, response):
        # 分析原创、翻唱、伴奏页面，提取当前页歌曲连接以及下一页
        self.logger.info('%s status code is %d' % (response.url, response.status))
        # item = response.meta['item']
        item = KugouItem()
        version = response.meta['version']

        song_list = re.findall('href="(http://5sing\.kugou\.com/\w{2}/\d{1,8}\.html)"', response.body_as_unicode())
        song_list_unique = list(set(song_list))
        song_list_unique.sort(key=song_list.index)

        for url in song_list_unique:
            new_item = KugouItem(item)  # 单个item变多item的时候 需要深复制
            yield Request(url, callback=self.parse_song, meta={'item': new_item})
            # yield Request(url, callback=self.parse_song, meta={'item': item})

        if version == 2:
            m = response.css('.page_message_clo+a::attr("href")').extract()
        else:
            m = re.findall('<a.*href="(/.*.html).*下一页.*a>', response.body_as_unicode())

        if m:
            next_url_path = m[0]
            next_page_url = response.urljoin(next_url_path)
            yield Request(next_page_url, callback=self.parse_lists, meta={'item': item, 'version': version})

    def parse_song(self, response):
        logging.info('parse_song_url:-----%s' % response.url)
        item = response.meta['item']

        item['song_name'] = response.css('.view_tit h1::text').extract()[0]
        item['song_url'] = response.url
        song_list = response.css('.mb15 li')

        temp = base64.b64decode(re.search('\"ticket\": \"(.*)\"', response.body_as_unicode()).group(1))
        json_object = json.loads(temp.decode())
        item['file_urls'] = [json_object['file']]

        for l in song_list:
            li_selector = l.css('::text').extract()

            try:
                # 非采集项或采集资料为空
                key = self.SONG_MAPPING[li_selector[0]]
                data = li_selector[1]
            except (KeyError, IndexError):
                pass

            if data is not None and data != '':
                if key == 'style':
                    data_filter = filter(lambda x: x != '', re.split('\s', data))
                    data = list(data_filter)
                    item[key] = data
                else:
                    item[key] = data.replace('\t', '')

        ins_m = re.search('<!--inspiration-->([\s\S]*)<!--inspiration-->', response.body_as_unicode())
        ins_temp = ins_m.group(1)
        ins_temp = re.sub('[\n\r]', '', ins_temp)
        ins = re.sub('(^\s*)|(\s*$)', '', ins_temp)
        item['inspiration'] = ins

        lrc_m = re.search('<!--lrc-->([\s\S]*)<!--lrc-->', response.body_as_unicode())
        lrc_temp = lrc_m.group(1)
        lrc_temp = re.sub('[\n\r]', '', lrc_temp)
        lrc = re.sub('(^\s*)|(\s*$)', '', lrc_temp)
        item['lrc'] = lrc

        callback_name = SpiderUtil.get_random_callback_name('kugou')
        _time = str(time.time() * 1000)[:13]
        # http://5sing.kugou.com/\w{2}/\d{1,8}.html
        song_type = response.url[23:25]
        song_id = response.url[26:-5]
        user_id = re.search('var OwnerUserID = ([0-9]*)', response.body_as_unicode()).group(1)
        _url = response.url

        yield FormRequest(
            'http://service.5sing.kugou.com/song/songDetailInit',
            method='GET',
            formdata={
                'jsoncallback': callback_name,
                'SongID': song_id,
                'UserID': user_id,
                'url': _url,
                'SongType': song_type,
                '_': _time
            },
            callback=self.parse_song_count,
            meta={'item': item}
        )

    def parse_song_count(self, response):
        item = response.meta['item']
        m = re.search('^jQuery[0-9_]*\((.*)\)$', response.body_as_unicode())
        song_detail_json = json.loads(m.group(1))
        song_dict = song_detail_json['song']
        like_dict = song_detail_json['like']
        item['song_popular'] = song_dict['totalrq']
        item['song_click'] = song_dict['totalclick']
        item['song_download_count'] = song_dict['totaldown']
        item['song_collect'] = song_dict['collect']
        item['song_like'] = like_dict['songlike']

        yield item

    @staticmethod
    def get_img_a_version(response):
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
