# -*- coding: utf-8 -*-

import datetime
from MySQLdb import *
from peewee import *

from .settings import MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWD

db = MySQLDatabase(MYSQL_DBNAME, user=MYSQL_USER, passwd=MYSQL_PASSWD)

class BaseModel(Model):
    class Meta:
        database = db

class ProGovWeb(BaseModel):
    provincial_depart = CharField()
    provincial_url = CharField()
    #class Meta:
    #    #create a unique together
    #    indexes =(
    #            (('searching_keyword', 'drop_down_keywords'), True),
    #            )

class CityCountryGovWeb(BaseModel):
    city_country_name = CharField()
    city_country_depart = CharField()
    city_country_url = CharField()

#class KeyInfo(BaseModel):
#    site = ForeignKeyField(Site, related_name='key_info')
#    creativity = CharField()
#    href = CharField()
#    is_advert = BooleanField(default=True)
#    created_time = DateTimeField(default=datetime.datetime.now)
