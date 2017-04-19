# -*- coding: utf-8 -*-

import re
import logging
from urlparse import urljoin

import scrapy
from scrapy.http import Request

from government.settings import HEADERS, LOGGING
from government.items import CityCountryItem

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('myspider')

class CcGovSpider(scrapy.Spider):
    name = "cc_gov"
    start_urls = [
            'http://haikou.gov.cn/',
            #'http://sanya.gov.cn/',
            'http://zwzx.sanya.gov.cn/zhengwu/sy_bm_bszn_lb.jsp',
            'http://lingao.gov.cn/',
            ]
    custom_settings = {
            'ITEM_PIPELINES': {
                    'government.pipelines.CityCountryPipeline': 300,
                    }
            }

    def __init__(self, *args, **kwargs):
    #    super(CcGovSpider, self).__init__(*args, **kwargs)
    #    self.start_urls = [kwargs.get('start_url', 'haikou.gov.cn')]
        self.headers = HEADERS

    def start_requests(self):

        for url in self.start_urls:
            print(url)
            yield Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        logger.debug('response.url: %s'%response.url)
        items = []
        if 'haikou' in response.url:
            text = response.xpath('//body/div/div[2]/div/div[2]/div[7]/div[5]/ul').extract()[0]
            for url, depart in re.findall(r'(\w+\.\w+\.\w+\.\w+\w+\.?).+\">(\W{1,15})</a>', text):
                item = CityCountryItem()
                item['city_country_name'] = '海口市'
                item['city_country_url'] = url
                item['city_country_depart'] = depart
                items.append(item)
        elif 'sanya' in response.url:
            #import pdb
            #pdb.set_trace()
            text = response.xpath('//body/div[2]/div[2]/div/div[2]/ul').extract()[0]
            for url, depart in re.findall(r'"(\S+)">?>\[(\S+)\]', text):
                item = CityCountryItem()
                item['city_country_name'] = '三亚市'
                item['city_country_url'] = urljoin('http://zwzx.sanya.gov.cn/zhengwu/', url)
                item['city_country_depart'] = depart
                items.append(item)
        elif 'lingao' in response.url:
            text = response.xpath('//body/div[4]/div[8]/div[2]/table[1]').extract()[0]
            for url, depart in re.findall(r'href="./(\S+)".+">(\W+)<', text):
                item = CityCountryItem()
                item['city_country_name'] = '临高县'
                item['city_country_url'] = urljoin('http://lingao.gov.cn/lg/', url)
                item['city_country_depart'] = depart
                items.append(item)

        import pprint
        pprint.pprint(items)
        return items

