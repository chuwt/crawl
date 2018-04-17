# coding: utf-8
"""
Created by chuwt on 18/4/2.
"""
# os

# third
from crawl import Task
# self
from resource.baidu_test import Test
from resource.baidu_test import WsTest, Bittrex


task = Task()
# task.add_task('test', Test())
# task.add_task('ws_test', WsTest())
task.add_task('bittrex', Bittrex())

if __name__ == '__main__':
    task.run()
