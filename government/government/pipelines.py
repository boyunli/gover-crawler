# -*- coding: utf-8 -*-

import datetime
import logging

from settings import LOGGING
from models import ProGovWeb, CityCountryGovWeb

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('myspider')

def before_request_handler():
    if not ProGovWeb.table_exists():
        ProGovWeb.create_table()
    if not CityCountryGovWeb.table_exists():
        CityCountryGovWeb.create_table()


class HainanGovPipeline(object):

    def process_item(self, item, spider):
        #import pdb
        #pdb.set_trace()
        before_request_handler()

        provincial_depart = item['provincial_depart']
        provincial_url = item['provincial_url']
        if provincial_url.endswith('.'):
            provincial_url += 'cn'
        logger.debug('\033[92m save depart:{0}, url:{1} \033[0m'
                .format(provincial_depart.encode('utf-8'), provincial_url.encode('utf-8')))
        try:
            gov, created = ProGovWeb.get_or_create(
                    provincial_depart=provincial_depart,
                    provincial_url=provincial_url,
                    )
        except Exception as e:
            logger.error(e)

        return item

class CityCountryPipeline(object):

    def process_item(self, item, spider):
        #import pdb
        #pdb.set_trace()
        before_request_handler()

        city_country_name = item['city_country_name']
        city_country_depart = item['city_country_depart']
        city_country_url = item['city_country_url']
        #if provincial_url.endswith('.'):
        #    provincial_url += 'cn'
        logger.debug('\033[92m depart:{0}, url:{1} \033[0m'
                .format(
                    city_country_depart.encode('utf-8'),
                    city_country_url.encode('utf-8')))
        try:
            city_country, created = CityCountryGovWeb.get_or_create(
                    city_country_name=city_country_name,
                    city_country_depart=city_country_depart,
                    defaults = {
                        'city_country_url':city_country_url,
                        },
                    )
            if not created:
                city_country.city_country_url = city_country_url
                #import pdb
                #pdb.set_trace()
                city_country.save()
        except Exception as e:
            logger.error(e)

        return item
