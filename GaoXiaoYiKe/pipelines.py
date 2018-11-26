# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from GaoXiaoYiKe import settings
import pymysql
from GaoXiaoYiKe.items import UserItem,ImageItem,CommentItem



class GaoxiaoyikePipeline(object):
    def process_item(self, item, spider):
        return item


class UserPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DBNAME,
            charset='utf8',
        )
        self.cursor = self.connect.cursor()
    def process_item(self,item,spider):
        #不同的pipeline对应不同的item
        if isinstance(item,UserItem):
            self.cursor.execute(
                '''
                insert into user(username,password,head_url) values(%s,%s,%s)
                ''', [item['username'], item['password'], item['head_url']
                      ]
            )
            self.connect.commit()
            return item

class ImagePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DBNAME,
            charset='utf8',
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if isinstance(item,ImageItem):
            self.cursor.execute(
                '''
                insert into image(url,user_id,create_date) values(%s,%s,%s)
                ''', [item['url'], item['user_id'], item['create_date']
                      ]
            )
            self.connect.commit()
            return item


class CommentPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DBNAME,
            charset='utf8',
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if isinstance(item,CommentItem):
            self.cursor.execute(
                '''
                insert into comment(content,image_id,user_id) values(%s,%s,%s)
                ''', [item['content'], item['image_id'], item['user_id']
                      ]
            )
            self.connect.commit()
            return item
