# coding: utf-8
"""
Created by chuwt on 18/4/2.
"""
# os

# third

# self
from crawl import Resource


class Test(Resource):
    def params(self):
        self.url = ['http://baidu.com', 'http://baidu.com', 'http://baidu.com', 'http://baidu.com', ]
        self.method = 'get'

    def magic(self, resp):
        print(resp)
        





