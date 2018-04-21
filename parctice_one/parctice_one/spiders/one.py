import scrapy
from scrapy import Request
from parctice_one.items import ParcticeOneItem
import time

#scrapy crawl par_one
class parctice_one(scrapy.Spider):
    name='par_one'
    def start_requests(self):
        url='http://www.mzitu.com/all/'
        yield scrapy.Request(
            url=url,
            callback=self.start_parse
        )
    
    def start_parse(self,response):
        urls=response.xpath('/html/body/div[2]/div[1]/div[2]/ul[4]/li[10]/p[2]//a/@href').extract()
        print(urls)
        for url in urls:
            yield Request(
                url=url,
                callback=self.parse
            )


    def parse(self,response):
        max_num=response.xpath('/html/body/div[2]/div[1]/div[4]/a[last()-1]/span/text()').extract_first(default='N/A')
        for num in range(0,int(max_num)+1):
            yield Request(
            url=response.url+'/'+'%s'%num,
            callback=self.img_urls,
            meta={
                'max_num':'%d'%int(max_num)
            }
            )

    def img_urls(self,response):
        item=ParcticeOneItem()
        item['image_folder']=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@alt').extract_first(default='N/A')+'%s'%response.meta['max_num']
        item['image_urls']=response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract()
        yield item
