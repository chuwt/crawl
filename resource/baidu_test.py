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
import time
order_id = 0
class Bittrex(Resource):
    def params(self):
        self.url = 'https://bittrex.com/api/v1.1/public/getmarkethistory?market=USDT-BTC'
        self.method = 'get'

    def magic(self, resp):
        data = json.loads(resp)
        for i in data['result']:
            print(i['Id'], order_id)
            if i['Id'] > order_id:
                print(i['OrderType'], i['Quantity'])
                if i['OrderType'] == 'BUY':
                    sell(i['Price'], i['Quantity']*100)
                    buy(i['Price'], i['Quantity'] * 100)
                # 下单
                else:
                    buy(i['Price'], i['Quantity']*100)
                    sell(i['Price'], i['Quantity']*100)
                time.sleep(5)
            else:
                continue
import requests
import json
trade_url = 'http://192.168.10.144:8088/asset/orders/limitOrder'
headers = {
        'authorization_token': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IndlaXRhb2NodUBnbWFpbC5jb20iLCJ0aW1lc3RhbXAiOiIxNTIzNTIzMDU0Ljc3MjkzMyIsInVpZCI6MTAwMDJ9.2tq4znzEAPPcYaVumokSNNNuKVooEpv0bJkJO_ptOfQ',
        'authorization_uid': '10002',
        'authorization_username': 'weitaochu@gmail.com',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65'
                      '.0.3325.162 Safari/537.36'
    }


def buy(price, amount):
    data = {"amount":str(amount),"market":"btc_usdt","price":str(price),"side":2,"source":""}
    data = json.dumps(data)
    r = requests.post(trade_url, data=data, headers=headers)
    print(r.text)


def sell(price, amount):
    data = {"amount":str(amount),"market":"btc_usdt","price":str(price),"side":1,"source":""}
    data = json.dumps(data)
    r = requests.post(trade_url, data=data, headers=headers)
    print(r.text)


class WsTest(Resource):
    def params(self):
        self.type = 'ws'
        self.url = 'ws://192.168.10.134:8082'
        self.send_msg = ['{"op": "<command>", "args": ["arg1", "arg2", "arg3"]}']

    def ws_magic(self, resp):
        print(resp)



