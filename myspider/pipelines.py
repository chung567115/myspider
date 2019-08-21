# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from myspider.spiders.dbhelper import DBHelper
from scrapy.utils.project import get_project_settings


class MyspiderPipeline(object):
    rate_map = {'很差': 1, '较差': 2, '还行': 3, '推荐': 4, '力荐': 5}
    
    def __init__(self):
        self.settings = get_project_settings()
        
        # 连接数据库
        if self.settings['SAVE_TO_DB']:
            self.db = DBHelper()
        pass
    
    def open_spider(self, spider):
        pass
    
    def process_item(self, item, spider):
        item['score'] = self.rate_map[item['score']]
        
        # 数据落库
        if self.settings['SAVE_TO_DB']:
            try:
                self.db.insert_to_db(item)
            except Exception as e:
                print(e)
                pass
        return item
    
    def close_spider(self, spider):
        self.db.close()
