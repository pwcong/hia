#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import time
import util
import urllib.request
import http.cookiejar


def make_opener(headers):
    cj = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cj)
    op = urllib.request.build_opener(cp)
    h = []

    for key, value in headers.items():
        elem = (key, value)
        h.append(elem)

    op.addheaders = h

    return op


def make_request(url, headers):
    req = urllib.request.Request(url)

    for key, value in headers.items():
        req.add_header(key, value)

    return req


def download_file(url, dir_path, opener = None):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = url.split('/')[-1]

    print('> start download ' + file_name + ' from ' + url)
    if opener is not None:

        with opener.open(url) as i:
            util.save_file(i.read(), dir_path, file_name)
            print('> download ' + file_name + ' successfully')

    else:
        with urllib.request.urlopen(url) as i:
            util.save_file(i.read(), dir_path, file_name)
            print('> download ' + file_name + ' successfully')


def download_files(urls, dir_path, opener = None):
    for url in urls:
        try:
            download_file(url, dir_path, opener)
            # 续一秒
            time.sleep(1)
        except:
            pass
