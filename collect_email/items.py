# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserEmailItem(scrapy.Item):
    __class__ = u'UserEmailItem'
    # define the fields for your item here like:
    index = scrapy.Field()
    username = scrapy.Field()
    email = scrapy.Field()
    asin = scrapy.Field()
    stars = scrapy.Field()
    page = scrapy.Field()
    product_at_page = scrapy.Field()
    product_index = scrapy.Field()
    keyword = scrapy.Field()

class AsinKeywordItem(scrapy.Item):
    __class__ = u'AsinKeywordItem'
    index = scrapy.Field()
    asin = scrapy.Field()
    keyword = scrapy.Field()

class AsinOfErrorItem(scrapy.Item):
    __class__ = u'AsinOfErrorItem'
    # id = scrapy.Field()
    # asin = scrapy.Field()
    # keyword = scrapy.Field()
    asin_keyword = scrapy.Field()
    redo = scrapy.Field()
