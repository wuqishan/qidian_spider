# -*- coding: utf-8 -*-
import scrapy
from qidian.items import ImagesItem

class Images(scrapy.Spider):
    name = 'images'
    allowed_domains = ['hk.lexiscn.com']
    start_urls = ['http://hk.lexiscn.com/']

    def parse(self, response):

        docs = response.xpath('//ul[@id="banner-l"]/li')
        if len(docs) > 0:
            for node in docs:
                item = ImagesItem()
                item['src'] = node.xpath('./img/@src').extract_first()
                yield item
