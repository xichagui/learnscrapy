#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

custom_settings = {
    'DOWNLOADER_MIDDLEWARES': {
        # 提供给request代理支持
        'zhuanqspider.middlewares.RandomUserAgent': 100,
        # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,#禁止内置的中间件
        'zhuanqspider.middlewares.JavaScriptDM': 543,
    },
    'ITEM_PIPELINES': {

    },
}