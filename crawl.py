# coding: utf-8
"""
Created by chuwt on 18/4/2.
"""
# os
import asyncio
import aiohttp
# third
import argparse
# self

# ARGS = argparse.ArgumentParser(descriptioin='A free proxy crawal')


class Resource:
    def __init__(self):
        self.data = ''
        self.url = ''
        self.method = ''
        self.headers = {}
        self.proxies = None

    def params(self):
        pass

    def magic(self, resp):
        pass

    async def fetch(self, url):
        """
        构造请求
        :return:
        """
        async with aiohttp.ClientSession() as session:
            if self.method == 'get':
                async with session.get(url, data=self.data, headers=self.headers, proxy=self.proxies) as resp:
                    data = await resp.text()
            elif self.method == 'post':
                async with session.get(url, data=self.data, headers=self.headers, proxy=self.proxies) as resp:
                    data = await resp.text()
            else:
                raise ValueError('method')
            return url, data

    async def work(self):
        """
        构造处理函数
        :return:
        """
        self.params()
        if isinstance(self.url, list):
            fetch = [asyncio.ensure_future(self.fetch(url)) for url in self.url]
            await asyncio.wait(fetch)
            data = [resp.result() for resp in fetch]
        else:
            fetch = [asyncio.ensure_future(self.fetch(self.url))]
            await asyncio.wait(fetch)
            url, data = fetch[0].result()
        self.magic(data)


class Task:
    def __init__(self):
        self.tasks = list()

    def add_task(self, name, resource):
        """
        name:
        resource:
        repeat:
        :return:
        """
        self.tasks.append(asyncio.ensure_future(resource.work()))

    async def main(self):
        await asyncio.wait(self.tasks)

    def run(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.ensure_future(self.main()))
        except Exception as msg:
            print(msg)
        finally:
            loop.close()



