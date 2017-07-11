#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

custom_settings = {
    'DOWNLOADER_MIDDLEWARES': {
        # 提供给request代理支持
        'zhuanqspider.middlewares.RandomUserAgent': 100,
    },
    # 'ROBOTSTXT_OBEY' : True,
    'ITEM_PIPELINES': {
        # 'zhuanqspider.pipelines.BilibiliPl': 300,
    },
}