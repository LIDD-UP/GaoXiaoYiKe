# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaoxiaoyikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserItem(scrapy.Item):
    username = scrapy.Field()
    password = scrapy.Field()
    head_url = scrapy.Field()


class ImageItem(scrapy.Item):
    url = scrapy.Field()
    user_id = scrapy.Field()
    create_date = scrapy.Field()


class CommentItem(scrapy.Item):
    content = scrapy.Field()
    image_id = scrapy.Field()
    user_id = scrapy.Field()


