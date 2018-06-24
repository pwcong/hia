#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
from bs4 import BeautifulSoup
from crawler.base import BaseCrawler
from util import request


class PangciCrawler(BaseCrawler):

    start_url = 'https://www.pangci.cc/works/'

    def crawl(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        textarea = soup.select_one('textarea.noshow')

        _soup = BeautifulSoup(textarea.get_text(), 'html.parser')

        imgs = _soup.select('.item .line .p img')
        img_urls = []

        for img in imgs:
            img_urls.append(img['src'])

        request.download_files(img_urls, self.dir_path, None)

        next_page = soup.select_one('.gopages .got .l a.page-next')
        if next_page is not None:
            next_url = next_page['href']
            self.crawl('https://www.pangci.cc' + next_url)
