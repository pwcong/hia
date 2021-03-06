#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
from bs4 import BeautifulSoup
from crawler.base import BaseCrawler
from util import request


class MiaotubaCrawler(BaseCrawler):

    start_url = 'http://www.miaotuba.com'

    headers = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.miaotuba.com',
        'Referer': 'http://www.miaotuba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    opener = None

    def __init__(self, browser, dir_path):
        self.opener = request.make_opener(self.headers)
        super().__init__(browser, dir_path)

    def get_filename_from_url(self, url):
      return url.split('/')[-1].split('&')[0]

    def crawl(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        imgs = soup.select('ul#post_container li.post .thumbnail img')
        img_urls = []

        for img in imgs:
            img_urls.append(img['src'])

        request.download_files(img_urls, self.dir_path, self.opener, self.get_filename_from_url)

        next_page = soup.select_one('.pagination a.next')
        if next_page is not None:
            next_url = next_page['href']
            self.crawl(next_url)
