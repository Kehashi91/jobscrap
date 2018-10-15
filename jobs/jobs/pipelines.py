# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.utils.project import get_project_settings
from scrapy.mail import MailSender



class JobsPipeline(object):

    def __init__(self):
        self.offers = []

    def process_item(self, item, spider):
        self.offers.append(item)
        return item

    def close_spider(self, spider):
        mailer = MailSender.from_settings(get_project_settings())

        msg = ""
        for count, item in enumerate(self.offers):
            msg += "oferta {}:\ncompany: {}\nsalary: {}\ntitle: {}\nrequirements: {}\n\n".format(count, item["company"], item["salary"], item["title"], item["requirements"])
        mailer.send(to=os.environ.get('MAIL_USERNAME'),subject="test",body=msg)
