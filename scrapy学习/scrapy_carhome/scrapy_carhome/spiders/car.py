import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["https://car.autohome.com.cn/price/brand-15.html"]
    # 注意如果你的请求的接口是html 结尾不应该加 /
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print('car程序正在执行')

        # 名字集合
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        # 价格集合
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')

        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)







