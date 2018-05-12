#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
from bs4 import BeautifulSoup
from crawler.base import BaseCrawler
from util import request


class JiandanCrawler(BaseCrawler):

    start_url = 'http://jiandan.net/ooxx'

    def crawl(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        imgs = soup.select('ol.commentlist li div.text a.view_img_link')
        img_urls = []

        for img in imgs:
            img_urls.append('http:' + img['href'])

        request.download_files(img_urls, self.dir_path)

        next_page = soup.select_one('a.previous-comment-page')
        if next_page is not None:
            next_url = next_page['href']
            self.crawl('http://' + next_url[2:])
