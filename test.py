# coding: utf-8
"""
Created by chuwt on 18/4/2.
"""
# os

# third
from crawl import Task
# self
from resource.baidu_test import Test


task = Task()
task.add_task('test', Test())

if __name__ == '__main__':
    task.run()
