# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import os.path
import hia.utils.url

class JiandanPipeline(object):
    def process_item(self, item, spider):

        if spider.name == "jiandan":

            save_dir = os.path.join(os.getcwd(), "res", "jiandan")

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            for img in item["imgs"]:

                try:
                    with urllib.request.urlopen(hia.utils.url.format_url(img)) as f:
                        if f.status == 200:
                            with open(os.path.join(save_dir, img.split("/")[-1]), "wb") as o:
                                o.write(f.read())

                except Exception as e:
                    print(e)

            return item

        return item
