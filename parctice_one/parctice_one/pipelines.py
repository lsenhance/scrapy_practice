# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import re

class ParcticeOnePipeline(object):
    def process_item(self, item, spider):
        return item
    
class MyImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item=request.meta['item']
        folder=item['image_folder']
        filename=u'/{0}/{1}'.format(folder,request.url.split('/')[-1])
        return filename
    

    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,
            headers={'referer':'http://www.mzitu.com'},
            meta={
                'item':item
            })

    def item_completed(self,results,item,info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths']=image_paths
        return item