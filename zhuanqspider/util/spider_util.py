#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import random

import time

__author__ = 'Cha'

class SpiderUtil(object):
    @staticmethod
    def get_random_callback_name():
        str_map = '0123456789' * 20
        str1 = 'jQuery17' + ''.join(random.sample(str_map, 17)) + '_' + str(time.time() * 1000)[:13]
        return str1