# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from win32com.client import Dispatch
import json

class QktswPipeline(object):
    def open_spider(self,spider):
        self.file = open("position.text","w",encoding="utf-8")

    def process_item(self, item, spider):
        dict_item = dict(item)
        thunder = Dispatch('ThunderAgent.Agent64.1')
        course_path = "F:\\迅雷下载"
        thunder.AddTask(dict_item["url"], dict_item["fileName"], course_path, "", "", -1, 0, 5)
        thunder.CommitTasks()
        json_str = json.dumps(dict_item,ensure_ascii=False)+"\n"
        self.file.write(json_str)
        return item
    def close_spider(self,spider):
        self.file.close()
