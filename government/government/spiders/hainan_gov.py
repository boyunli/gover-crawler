# -*- coding: utf-8 -*-

import re
import logging
import logging.config

import scrapy
from scrapy.http import Request

from government.settings import HEADERS, LOGGING
from government.items import ProvItem

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('myspider')



class HainanGoverSpider(scrapy.Spider):
    name = "hainan_gov"
    allowed_domains = ["hainan.gov.cn"]
    start_urls = ['http://hainan.gov.cn/']
    custom_settings = {
            'ITEM_PIPELINES': {
                    'government.pipelines.HainanGovPipeline': 300,
                    }
            }

    def __init__(self):
        self.headers = HEADERS

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        text = response.xpath('//body/div/div[3]/div/div[6]/div/ul/li[4]/div/div').extract()[0]
        items = []
        #import pdb
        #pdb.set_trace()
        for url, depart  in re.findall(r'(\w+\.\w+\.\w+\.\w+\w+\.?).+&\w+\W\s(\W+)<', text):
            item = ProvItem()
            item['provincial_url'] = url
            item['provincial_depart'] = depart
            items.append(item)
        import pprint
        pprint.pprint(items)
        return items

