# -*- coding: utf-8 -*-
import scrapy
from GaoXiaoYiKe.items import UserItem
import random
from random import choice


class CrawlUserSpider(scrapy.Spider):
    name = 'crawl_user'
    allowed_domains = ['bx1k.com']
    start_urls = ['http://www.bx1k.com/dryhumor/']

    def parse(self, response):
        users = response.css('.jokeit  li')
        for user in users:
            username = user.css('.jokeall .jokeuser a::text').extract()[1].strip()

            head_url = user.css('.jokeall .jokeuser a img::attr(src)').extract_first()
            password = choice([1,2,3,4])
            user_item = UserItem()
            user_item['username'] = username
            user_item['password'] = password
            user_item['head_url'] = head_url
            yield user_item
        for i in range(50,80):
            next_url = 'http://www.bx1k.com/dryhumor/list-p-{}.html'.format(i)
            yield scrapy.Request(url=next_url,callback=self.parse)

