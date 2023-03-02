import scrapy

from scrapy_dangdang.items import ScrapyDangdangItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = 'http://category.dangdang.com/pg'
    page = 1



    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # src = //ul[@id="component_59"]/li//img/@src
        #         alt = //ul[@id="component_59"]/li//img/@alt
        #         price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 所有的selector的对象都可以再次调用xpath方法
        li_list = response.xpath('////ul[@id="component_59"]/li')
        for li in li_list:

            src = li.xpath('//img/@data-original').extract_first()
            # 第一张图片和其他图片的标签的属性是不一样的
            # 第一张图片的src是可以使用的,其他的图片的地址是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdangItem(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book

