# -*- coding: utf-8 -*-
import scrapy
from tools.sql_connect_tools import SQLConnectTools
from GaoXiaoYiKe.items import ImageItem,CommentItem
import datetime


class CrawlCommentSpider(scrapy.Spider):
    name = 'crawl_comment'
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
        contents = response.css('.com-list .cf .com-info .com-txt').extract()[0]
        # 他这里的id可能是通过渲染得来得；xpath取不到；
        # url2 = response.xpath("//ul[@id='thumb-ul']/li")
        sql_connect_tools = SQLConnectTools()
        for content in contents():
            user_id = sql_connect_tools.get_user_id()
            image_id = sql_connect_tools.get_image_id()
            comment_item = CommentItem()
            comment_item['content'] = content
            comment_item['user_id'] = user_id
            comment_item['image_id'] = image_id
            yield comment_item

