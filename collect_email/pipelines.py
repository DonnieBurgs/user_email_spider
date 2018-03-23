# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from collect_email.db_manage import sessionmaker, UserEmails, AsinKeyword, AsinOfError, engine
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()

class UserEmailPipeline(object):
    def process_item(self, item, spider):

        if item.__class__ == u'UserEmailItem':
            result = UserEmails(**item)
            session.add(result)
            try:
                session.commit()
            except Exception as e:
                logging.exception('=== error in pipeline ===')
                session.rollback()

        elif item.__class__ == u'AsinKeywordItem':
            result = AsinKeyword(**item)
            session.add(result)
            try:
                session.commit()
            except Exception as e:
                logging.exception('=== error in pipeline ===')
                session.rollback()
        elif item.__class__ == u'AsinOfErrorItem':
            result = AsinOfError(**item)
            session.add(result)
            try:
                session.commit()
            except Exception as e:
                logging.exception('=== error in pipeline ===')
                session.rollback()