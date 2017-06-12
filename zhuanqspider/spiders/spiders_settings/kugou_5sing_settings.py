custom_settings = {
    'DOWNLOADER_MIDDLEWARES': {
        # 提供给request代理支持
        'zhuanqspider.middlewares.RandomUserAgent': 100,
    },
    # 'ROBOTSTXT_OBEY' : True,
    'ITEM_PIPELINES': {
        # 'zhuanqspider.pipelines.Kugou5singPl': 300,
        'scrapy.pipelines.files.FilesPipeline': 1
    },
}

