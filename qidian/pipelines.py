# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem


class QidianPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagesDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # print(item, info, 111)
        yield scrapy.Request(item['src'])
        # for image_url in item['image_urls']:
        #     yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        # print(results, item, info)
        # image_paths = [x['src'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths

        return item
