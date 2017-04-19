# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provincial_depart = scrapy.Field()
    provincial_url = scrapy.Field()


class CityCountryItem(scrapy.Item):
    city_country_name = scrapy.Field()
    city_country_depart = scrapy.Field()
    city_country_url = scrapy.Field()
