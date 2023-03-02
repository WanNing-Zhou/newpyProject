import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
# 1 srcapy项目的结构
    # 项目名字
        # 项目名字
          # spiders文件夹(存储的是爬虫文件)
            # init
            # 自定以的爬虫文件 功能文件
          #   init
          #   items 定义数据结构的地方(爬取的数据都包含哪些)
            # middleware 中间件 代理
            # piplines 管道(用来处理下载数据)
            # settings 配置文件(robots 协议 ua 都在这里定义)

    def parse(self, response):
        # 字符串
        # content = response.text
        # 二进制数据
        # content = response.body

        # 可以直接使用xpath方法来解析内容
        # content = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        # print('content的值为', content)
        # 提取selector对象的data属性值
        # print('selector对象的data属性值', response.extract())
        # 提取selector列表的第一数据
        print('提取seletor列表的第一个数据', response.extract_first())





