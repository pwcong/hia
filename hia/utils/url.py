# -*- coding: utf-8 -*-

import re

def format_url(url):
    res = re.match("http:.+", url)

    if res is None:
        return "http:" + url
    
    return url

def get_filename(url):
    return url.split("/")[-1]


