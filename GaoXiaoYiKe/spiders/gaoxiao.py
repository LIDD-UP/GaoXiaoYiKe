# -*- coding: utf-8 -*-
import scrapy


class GaoxiaoSpider(scrapy.Spider):
    name = 'gaoxiao'
    allowed_domains = ['bx1k.com']
    start_urls = ['http://www.bx1k.com/funnyimg/find-cate-1-p-1.html']

    def parse(self, response):
        images = response.css('.listcont .plist li')
        for image in images:
            # css写法
            detail_url = image.css('a::attr(href)').extract_first()
            # xpath写法
            detail_url = image.xpath('//a/@href').extract_first()
            # 不需要meta信息了，直接在详情页取数据
            scrapy.Request(url=detail_url,callback=self.parse)


    # 爬取详情页的数据
    def parse_content(self,response):
        pass
        username =
        password =
        head_url =
        #
        #
        # url =
        # user_id =
        # create_date =
        #
        #
        # content =
        # image_id =
        # user_id =

