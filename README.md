# crawl
a convenient web crawl proj

这是一个方便编写异步爬虫的应用工具，仿照flask风格编写

# todo list
- 完善websocket 方式，目前只支持一次性发送，类似返回ping的时候并不会发送pong
- 增加定时请求和循环请求
- 其他想到再加

### example

    from crawl import Task
    from crawl import Resource

	class Test(Resource):
	    def params(self):
	        # 配置url, method 等请求参数
	        self.url = 'http://baidu.com'
	        self.method = 'get'

        def magic(self, resp):
            # 请求返回，编写自己的处理函数
            print(resp)

	task = Task()
	task.add_task('test', Test())
	task.run()

### websocket example

    class WsTest(Resource):
        def params(self):
            self.type = 'ws'
            self.url = 'ws://121.40.165.18:8088'
            self.send_msg = ['{"op": "<command>", "args": ["arg1", "arg2", "arg3"]}']

        def ws_magic(self, resp):
            print(resp)



# Donation
   - BTC: 1D1nXVy1nRhSMN6dYh4MgMSXiMXgVS7cW3
   - BCH: 1D1nXVy1nRhSMN6dYh4MgMSXiMXgVS7cW3
   - ETH: 0x5d6ca1adc871710f68a648d315e5aed6a427936a

