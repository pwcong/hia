#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
from bs4 import BeautifulSoup
from crawler.base import BaseCrawler
from util import request


class MzituCrawler(BaseCrawler):

    start_url = 'http://www.mzitu.com'

    def crawl(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        imgs = soup.select('ul#pins li img')
        img_urls = []

        for img in imgs:
            img_urls.append(img['data-original'])

        request.download_files(img_urls, self.dir_path)

        next_page = soup.select_one('a.next.page-numbers')
        if next_page is not None:
            next_url = next_page['href']
            self.crawl(next_url)
