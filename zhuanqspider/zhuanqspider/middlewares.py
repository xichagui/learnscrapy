# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import logging

# import pymongo
import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver


class ZhuanqSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""
    '''随机浏览器'''
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        #print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))

class SimpleHttpProxyDM(object):
    def __init__(self, simple_proxy_ip):
        self.proxy = simple_proxy_ip

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            simple_proxy_ip=crawler.settings.getlist('SIMPLE_PROXY_IP'),
        )

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy)
        # if not proxy["valid"]:
        #     self.inc_proxy_index()
        #     proxy = self.proxyes[self.proxy_index]

        if proxy["ip"]:
            request.meta["proxy"] = "http://%s:%s" % (proxy['ip'], proxy['port'])

    def process_exception(self, request, exception, spider):
        logging.info("exception for %s %s " % (request.meta["proxy"], exception))
        new_request = request.copy()
        new_request.dont_filter = True
        return new_request


class HttpProxyDM(object):
    def __init__(self, ip_pool, mongo_uri, mongo_db, mongo_collection):
        self.ip_pool = ip_pool

        self.proxies = [{"proxy": None, "valid": True, "count": 0}]
        self.proxy_index = 0

        logging.debug('MyProxyMiddleware init')
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

        self.per_count = 0
        self.pool_size = 0

        '''从mongo数据库中读取可用代理ip'''
        try:
            self.proxy_ip_pool_from_DB = self.collection.find({})
            self.pool_size = self.collection.count({})
            logging.debug('Get proxyippool from MongoDB')
        except:
            logging.error('Get proxyippool from MongoDB error')
        finally:
            self.client.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            ip_pool = crawler.settings.getlist('IP_POOL'),
            mongo_uri = crawler.settings.get('MONGODB_URI'),
            mongo_db = crawler.settings.get('MONGODB_DB'),
            # 2号数据库
            mongo_collection = crawler.settings.get('MONGODB_COLLECTION_PROXY2')
        )

    def process_request(self, request, spider):
        # self.proxy_index = 0

        # if "change_proxy" in request.meta.keys() and request.meta["change_proxy"]:
        #     logging.info("change proxy request get by spider: %s" % request)
            # self.invalid_proxy(request.meta["proxy_index"])
            # request.meta["change_proxy"] = False

        self.set_proxy(request)
        # elif self.ip_pool != None:
        #     proxy_ip = random.choice(self.ip_pool)
        #     logging.info("------use the proxy ip: %s:%s" % (proxy_ip['ip'], proxy_ip['port']) )
        #     request.meta["proxy"] = "http://%s:%s" % (proxy_ip['ip'], proxy_ip['port'])

    def process_response(self, request, response, spider):
        """
            检查response.status, 根据status是否在允许的状态码中决定是否切换到下一个proxy, 或者禁用proxy
        """
        if "proxy" in request.meta.keys():
            logging.debug("%s %s %s" % (request.meta["proxy"], response.status, request.url))
        else:
            logging.debug("None %s %s" % (response.status, request.url))

        if response.status == 200:
            self.per_count += 1
            if self.per_count >= 5:
                self.per_count = 0
                self.proxy_index += 1

        if response.status != 200:
            logging.debug("%s for %s change IP" % (response.status, request.url))
            new_request = request.copy()
            new_request.dont_filter = True
            self.per_count = 0
            self.proxy_index += 1
            return new_request
        else:
            return response




    def process_exception(self, request, exception, spider):
        logging.info("exception for %s %s " % (request.meta["proxy"], exception))
        new_request = request.copy()
        new_request.dont_filter = True
        # proxy_ip = random.choice(self.ip_pool)
        # logging.info("------change proxy ip: %s:%s" % (proxy_ip['ip'], proxy_ip['port']) )
        # new_request.meta["proxy"] = "http://%s:%s" % (proxy_ip['ip'], proxy_ip['port'])

        self.per_count = 0
        self.proxy_index += 1

        self.set_proxy(new_request)
        return new_request

    def set_proxy(self, request):
        """
        设置代理
        """
        proxy = self.proxy_ip_pool_from_DB[self.proxy_index % self.pool_size]

        # if not proxy["valid"]:
        #     self.inc_proxy_index()
        #     proxy = self.proxyes[self.proxy_index]

        if proxy["ip"]:
            request.meta["proxy"] = "http://%s:%s" % (proxy['ip'], proxy['port'])
        # elif "proxy" in request.meta.keys():
        #     del request.meta["proxy"]
        # request.meta["proxy_index"] = self.proxy_index
        # proxy["count"] += 1

class seleniumDM(object):

    @classmethod
    def process_request(cls, request, spider):
        if 'PhantomJS' in request.meta:
            driver = webdriver.PhantomJS()
            driver.implicitly_wait(3)
            driver.get(request.url)
            body = driver.page_source.encode('utf-8')
            url = driver.current_url
            response = HtmlResponse(url, body=body, encoding='utf-8', request=request)
            driver.quit()
            return response