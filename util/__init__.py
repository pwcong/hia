#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import gzip


def ungzip(data):
    try:
        data = gzip.decompress(data)
    except Exception as e:
        print(e)
    return data

def save_file(input_stream, dir_path, file_name):
    with open(os.path.join(dir_path, file_name), 'wb') as o:
        o.write(input_stream)