#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import random

import time

__author__ = 'Cha'


class SpiderUtil(object):
    @staticmethod
    def get_random_callback_name(site=''):
        n = 18
        if site == 'kugou':
            n = 17
        elif site == 'bilibili':
            n = 18
        str_map = '0123456789' * 20
        str1 = 'jQuery17' + ''.join(random.sample(str_map, n)) + '_' + str(time.time() * 1000)[:13]
        return str1
