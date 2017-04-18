# -*- coding: utf-8 -*-

import datetime
import logging

from settings import LOGGING
from models import ProGovWeb

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('myspider')

def before_request_handler():
    if not ProGovWeb.table_exists():
        ProGovWeb.create_table()


class GovWebPipeline(object):

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
