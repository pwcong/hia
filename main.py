#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import sys
import json
from selenium import webdriver

from crawler.jiandan import JiandanCrawler
from crawler.mzitu import MzituCrawler
cwd_path = os.getcwd()

crawlers = {
    'jiandan': JiandanCrawler,
    'mzitu': MzituCrawler
}


def get_config():

    config_path = os.path.join(cwd_path, 'hia.config.json')

    if not os.path.exists(config_path):
        return {
            'webDriver': {
                'name': 'Chrome',
                'path': 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
            }
        }

    with open(config_path) as i:
        config = json.load(i)
        print('\n> load configuration from ' + config_path + '\n')
        return config


def main():

    argv = sys.argv
    if len(argv) < 2:
        print('\n*** Lack of crawler name ***\n\nUsage: python main.py <crawler>\n')
        exit(1)

    crawler = argv[1]
    if crawlers.get(crawler) is None:
        print('\n*** Unknown crawler ***\n')
        exit(1)

    config = get_config()

    print('> open browser\n')
    browser = webdriver.Chrome(config['webDriver']['path'])

    dir_path = os.path.join(os.getcwd(), 'imgs', crawler)

    print('> start crawl\n')
    crawlers.get(crawler)(browser, dir_path)
    print('> finish crawl')


if __name__ == '__main__':
    main()
