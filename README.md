# crawl
a convenient web crawl proj

这是一个方便编写异步爬虫的应用工具，仿照flask风格编写
###example
	from crawal	import Task, Resource


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


# Donation
   - BTC: 1D1nXVy1nRhSMN6dYh4MgMSXiMXgVS7cW3
   - BCH: 1D1nXVy1nRhSMN6dYh4MgMSXiMXgVS7cW3
   - ETH: 0x5d6ca1adc871710f68a648d315e5aed6a427936a