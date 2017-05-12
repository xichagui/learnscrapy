# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import logging
from scrapy import signals


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

class HttpProxyDM(object):
    def __init__(self, ip_pool):
        self.ip_pool = ip_pool
        self.proxies = [{"proxy": None, "valid": True, "count": 0}]
        self.proxy_index = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('IP_POOL'))

    def process_request(self, request, spider):
        self.proxy_index = 0

        # if "change_proxy" in request.meta.keys() and request.meta["change_proxy"]:
        #     logging.info("change proxy request get by spider: %s" % request)
            # self.invalid_proxy(request.meta["proxy_index"])
            # request.meta["change_proxy"] = False

        if self.ip_pool != None:
            proxy_ip = random.choice(self.ip_pool)
            logging.info("------use the proxy ip: %s:%s" % (proxy_ip['ip'], proxy_ip['port']) )
            request.meta["proxy"] = "http://%s:%s" % (proxy_ip['ip'], proxy_ip['port'])


    def process_exception(self, request, exception, spider):
        logging.info("exception for %s " % request.url)
        new_request = request.copy()
        proxy_ip = random.choice(self.ip_pool)
        logging.info("------change proxy ip: %s:%s" % (proxy_ip['ip'], proxy_ip['port']) )
        new_request.meta["proxy"] = "http://%s:%s" % (proxy_ip['ip'], proxy_ip['port'])
        return new_request