# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    head_url = models.CharField(max_length=200)
    fans_num = models.BigIntegerField()
    popular = models.BigIntegerField()

    kugou_url = models.URLField(blank=True)

    kugou_is_vip = models.BooleanField(default=False)
    kugou_is_realname = models.BooleanField(default=False)
    kugou_is_tao = models.BooleanField(default=False)
    kugou_is_musician = models.BooleanField(default=False)
    kugou_is_liver = models.BooleanField(default=False)
    kugou_is_recommend = models.BooleanField(default=False)
    kugou_is_star = models.BooleanField(default=False)
    kugou_is_mobile = models.BooleanField(default=False)
    kugou_is_xinlang = models.BooleanField(default=False)
    kugou_is_renren = models.BooleanField(default=False)

class Style(models.Model):
    name = models.CharField(max_length=20)

class Work(models.Model):
    title = models.CharField('标题', max_length=200)
    singer = models.ManyToManyField(Author, blank=True, related_name='singer')  # 歌手
    lyricist = models.ManyToManyField(Author, blank=True, related_name='lyricist')  # 词作
    composer = models.ManyToManyField(Author, blank=True, related_name='composer')  # 编曲
    arrange = models.ManyToManyField(Author, blank=True, related_name='arrange')
    mixer = models.ManyToManyField(Author, blank=True, related_name='mixer')
    type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    style = models.ManyToManyField(Style)
    upload_time = models.DateTimeField()
    original_singer = models.ManyToManyField(Author, blank=True, related_name='original_singer')
    lrc = models.TextField(max_length=500)
    inspiration = models.TextField(max_length=1000)
    song_popular = models.BigIntegerField()
    song_click = models.BigIntegerField()
    song_download_count = models.BigIntegerField()
    song_collect = models.BigIntegerField()
    song_like = models.BigIntegerField()
    song_url = models.URLField()

    # title = models.CharField(max_length=100)  # 博客标题
    # category = models.ForeignKey(Category)  # 分类,外键
    # tag = models.ManyToManyField(Tag, blank=True)  # 标签,多对多关系
    # # date_time = models.DateTimeField()  # 日期
    #
    # # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    # created_time = models.DateTimeField(auto_now_add=True)
    # modified_time = models.DateTimeField(auto_now=True)
    #
    # content = models.TextField(blank=True, null=True)  # 正文
    # excerpt = models.CharField(max_length=200, blank=True)  # 摘要

    # class KugouItem(scrapy.Item):
    #     # define the fields for your item here like:
    #     # name = scrapy.Field()
    #     # 个人信息
    #
    #     # 昵称
    #     kugou_name = scrapy.Field()
    #     # 粉丝数
    #     kugou_fans = scrapy.Field()
    #     # 人气
    #     kugou_popular = scrapy.Field()
    #     # 头像链接
    #     kugou_img = scrapy.Field()
    #     # 签名
    #     kugou_sign = scrapy.Field()
    #     # 5sing首页url
    #     kugou_url = scrapy.Field()
    #     '''
    #         5sing图标
    #         会员、实名、淘歌达人、音乐人、live资格、推荐歌手、明星会员、手机客户端、微博、人人网
    #     '''
    #     is_vip = scrapy.Field()
    #     is_realname = scrapy.Field()
    #     is_tao = scrapy.Field()
    #     is_musician = scrapy.Field()
    #     is_liver = scrapy.Field()
    #     is_recommend = scrapy.Field()
    #     is_star = scrapy.Field()
    #     is_mobile = scrapy.Field()
    #     is_xinlang = scrapy.Field()
    #     is_renren = scrapy.Field()
    #
    #     # 歌曲信息
    #     song_name = scrapy.Field()
    #     singer = scrapy.Field()
    #     lyricist = scrapy.Field()
    #     composer = scrapy.Field()
    #     arrange = scrapy.Field()
    #     mixer = scrapy.Field()
    #     type = scrapy.Field()
    #     language = scrapy.Field()
    #     style = scrapy.Field()
    #     download = scrapy.Field()
    #     upload_time = scrapy.Field()
    #     original_singer = scrapy.Field()
    #     lrc = scrapy.Field()
    #     inspiration = scrapy.Field()
    #     song_popular = scrapy.Field()
    #     song_click = scrapy.Field()
    #     song_download_count = scrapy.Field()
    #     song_collect = scrapy.Field()
    #     song_like = scrapy.Field()
    #     song_url = scrapy.Field()
    #     file_urls = scrapy.Field()
    #     files = scrapy.Field()
    #     file_path = scrapy.Field()