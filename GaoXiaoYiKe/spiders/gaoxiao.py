# -*- coding: utf-8 -*-
import scrapy
from tools.sql_connect_tools import SQLConnectTools
from GaoXiaoYiKe.items import ImageItem,CommentItem
import datetime


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
            # detail_url = image.xpath('//a/@href').extract_first()
            # 不需要meta信息了，直接在详情页取数据
            # image_url= image.css('img::attr(data-src)')
            yield scrapy.Request(url=detail_url,callback=self.parse_content)
        for i in range(50):
            next_url = 'http://www.bx1k.com/funnyimg/find-cate-1-p-{}.html'.format(i)
            yield scrapy.Request(url=next_url,callback=self.parse)


    # 爬取详情页的数据
    def parse_content(self,response):
        print(response.text)
        # 这里出现问题是由于没有登陆得原因；
        url = response.css('ul#thumb-ul li img::attr(big_src)').extract()[0]
        # 他这里的id可能是通过渲染得来得；xpath取不到；
        # url2 = response.xpath("//ul[@id='thumb-ul']/li")
        user_id = SQLConnectTools.get_user_id()
        create_date = datetime.datetime.now()
        image_item = ImageItem()
        image_item['url'] = url
        image_item['user_id'] = user_id
        image_item['create_date'] = create_date
        yield image_item



