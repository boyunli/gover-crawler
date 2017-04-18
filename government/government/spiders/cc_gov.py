# -*- coding: utf-8 -*-
import scrapy


class CcGovSpider(scrapy.Spider):
    name = "cc_gov"

    def __init__(self, *args, **kwargs):
        super(CcGovSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url', 'haikou.gov.cn')]

    def parse(self, response):
        pass
