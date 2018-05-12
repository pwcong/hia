#!/usr/bin/env python3
# -*- coding: utf8 -*-


class BaseCrawler:

    start_url = ''
    browser = None
    dir_path = ''

    def __init__(self, browser, dir_path):
        self.browser = browser
        self.dir_path = dir_path
        self.crawl(self.start_url)

    def get_html(self, url):
        self.browser.get(url)
        return self.browser.page_source

    def crawl(self, url):
        pass
