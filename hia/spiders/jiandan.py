# -*- coding: utf-8 -*-

import scrapy
from hia.items import JiandanItem

class JiandanSpider(scrapy.Spider):
    name = "jiandan"

    start_urls = [
        "http://jandan.net/ooxx"
    ]

    def parse(self, response):
        for li in response.css("div#comments ol.commentlist li"):

            item = JiandanItem()

            item["author"] = li.css("div.author strong::text").extract_first()
            item["imgs"] = li.css("div.text p img::attr(src)").extract()

            yield item

        next_page = response.css("div.cp-pagenavi a.previous-comment-page::attr(href)").extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)