# coding: utf-8
"""
Created by chuwt on 18/4/2.
"""
# os
import asyncio
import aiohttp
# third
import uvloop
import argparse
# self

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# ARGS = argparse.ArgumentParser(descriptioin='A free proxy crawal')


class Resource:
    def __init__(self):
        self.type = 'http'
        self.url = ''
        self.method = ''
        self.headers = dict()
        self.proxies = None
        self.send_msg = list()
        self.data = ''

    def params(self):
        pass

    def magic(self, resp):
        pass

    def ws_magic(self, resp):
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

    async def ws_fetch(self, url):
        async with aiohttp.ClientSession().ws_connect(url) as ws:
            for sender_msg in self.send_msg:
                await ws.send_str(sender_msg)
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    self.ws_magic(msg.data)
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    await ws.close()
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    await ws.close()

    async def work(self):
        """
        构造处理函数
        :return:
        """
        self.params()
        if self.type.startswith('ws'):
            task = list()
            task.append(asyncio.ensure_future(self.ws_fetch(self.url)))
            await asyncio.wait(task)
        else:
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



