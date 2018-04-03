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
        

class WsTest(Resource):
    def params(self):
        self.type = 'ws'
        self.url = 'http://localhost:8888/ws'
        self.send_msg = ['{"id":2,"method":"state.subscribe","params":{"marketlist":["btc_usdt","eth_usdt","eth_btc"]}}']
        # self.send_msg = ['{"op": "<command>", "args": ["arg1", "arg2", "arg3"]}']

    def ws_magic(self, resp):
        print(resp)



