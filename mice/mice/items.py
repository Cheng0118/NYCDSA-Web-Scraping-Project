# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MiceItem(scrapy.Item):
    name = scrapy.Field()
    model = scrapy.Field()
    brand = scrapy.Field()
    style = scrapy.Field()
    ctype = scrapy.Field()
    dpi = scrapy.Field()
    buttons = scrapy.Field()
    color = scrapy.Field()
    reviews = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()