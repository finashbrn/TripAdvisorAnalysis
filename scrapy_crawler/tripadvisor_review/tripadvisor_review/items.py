# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	restaurant = scrapy.Field()
	city = scrapy.Field()
	rating = scrapy.Field()
	price = scrapy.Field()
	title_review = scrapy.Field()
	review_desc = scrapy.Field()
    #pass
