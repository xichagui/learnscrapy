# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KugouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 个人信息

    # 昵称
    kugou_name = scrapy.Field()
    # 粉丝数
    kugou_fans = scrapy.Field()
    # 人气
    kugou_popular = scrapy.Field()
    # 头像链接
    kugou_img = scrapy.Field()
    # 签名
    kugou_sign = scrapy.Field()
    # 5sing首页url
    kugou_url = scrapy.Field()
    '''
        5sing图标
        会员、实名、淘歌达人、音乐人、live资格、推荐歌手、明星会员、手机客户端、微博、人人网
    '''
    is_vip = scrapy.Field()
    is_realname = scrapy.Field()
    is_tao = scrapy.Field()
    is_musician = scrapy.Field()
    is_liver = scrapy.Field()
    is_recommend = scrapy.Field()
    is_star = scrapy.Field()
    is_mobile = scrapy.Field()
    is_xinlang = scrapy.Field()
    is_renren = scrapy.Field()

    # 歌曲信息
    song_name = scrapy.Field()
    singer = scrapy.Field()
    lyricist = scrapy.Field()
    composer = scrapy.Field()
    arrange = scrapy.Field()
    mixer = scrapy.Field()
    type = scrapy.Field()
    language = scrapy.Field()
    style = scrapy.Field()
    download = scrapy.Field()
    upload_time = scrapy.Field()
    original_singer = scrapy.Field()
    lrc = scrapy.Field()
    inspiration = scrapy.Field()
    song_popular = scrapy.Field()
    song_click = scrapy.Field()
    song_download_count = scrapy.Field()
    song_collect = scrapy.Field()
    song_like = scrapy.Field()
    song_url = scrapy.Field()
    file_url = scrapy.Field()

class BilibiliItem(scrapy.Item):
    # b站昵称、头像、签名、粉丝数、播放数、空间地址、mid、生日、公告
    bilibili_name = scrapy.Field()
    bilibili_img = scrapy.Field()
    bilibili_sign = scrapy.Field()
    bilibili_fans = scrapy.Field()
    bilibili_play = scrapy.Field()
    bilibili_url = scrapy.Field()
    bilibili_mid = scrapy.Field()
    bilibili_birthday = scrapy.Field()
    bilibili_notice = scrapy.Field()
    bilibili_sex = scrapy.Field()
    bilibili_regtime = scrapy.Field()

    # 视频信息
    title = scrapy.Field()
    play = scrapy.Field()
    pic = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    aid = scrapy.Field()
    favorites = scrapy.Field()
    length = scrapy.Field()
    created = scrapy.Field()
    typeid = scrapy.Field()
    comment = scrapy.Field()
    coin = scrapy.Field()
    video_url = scrapy.Field()
    tags = scrapy.Field()

    #多p视频列表
    video_list = scrapy.Field()





