import scrapy

import json

class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ['http://fanyi.baidu.com/sug']
    # post 请求 如果美誉偶参数,那么这个请求将没有任何意义
    # 所以start_urls 也米有用了
    # parse方法也没有用了
    # start_urls = ["http://fanyi.baidu.com/"]

    # def parse(self, response):
    #     pass

    def start_request(self):
        url = 'http://fanyi.baidu.com/sug'

        data = {
            'kw' : 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)


    def parse_second(self,response):
        content = response.text
        obj = json.loads(content)
        # print(content)
        print(obj)