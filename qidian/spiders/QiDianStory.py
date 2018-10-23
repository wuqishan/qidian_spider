# -*- coding: utf-8 -*-
import scrapy


class QiDianStorySpider(scrapy.Spider):
    name = 'qidianstory'
    allowed_domains = ['www.qidian.com']
    start_urls = ['http://www.qidian.com/']
    #
    # def __init__(self, name=None, **kwargs):
    #     super(QiDianStorySpider, self).__init__(self, name=None, **kwargs)
    #
    #     # pass


    def parse(self, response):

        docs = response.xpath('//div[@id="classify-list"]/dl/dd')
        if len(docs) > 0:
            for node in docs:
                item = {}
                item['href'] = node.xpath('./a/@href').extract_first()
                item['name'] = node.xpath('./a//span[@class="info"]/i/text()').extract_first()
                item['number'] = node.xpath('./a//span[@class="info"]/b/text()').extract_first()
                yield item
