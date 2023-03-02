import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['cn.58.com']
    start_urls = ['http://cn.58.com/']

    def parse(self, response):
        pass
