# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


# 如果想使用管道的话,那么就必须在settings中开启管道
class ScrapyDangdangPipeline:
    # 在爬虫文件开始执行之前执行
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')
        self.fp.write('[')
        # print('-----')

    # item 就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式不推荐,因为每传递过来一个对象,那么就打开一次文件,对文件的操作过于频繁
        # 将数据保存到文件中
        # 1) write方法必须要写一个字符串,而不能是其他的对象
        # 2) w 模式会每一个对象都打开一个文件 覆盖之前的内容
        # with open('book.json', 'a', encoding='utf-8') as fp:
        self.fp.write(str(item))
        # st = json.dumps(item)
        # print('item',st)
        # self.fp.write(json.dumps(item))

        return item

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        self.fp.write(']')
        self.fp.close()

        # print('++++++++')
