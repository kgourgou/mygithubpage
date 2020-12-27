#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2017 KG

"""

$ python new-post "title of the post"

new-post can also be executed directly:

$ new-post "title of the post"

"""

import argparse
import time
import uuid

def main():
    parser = argparse.ArgumentParser(description='Jekyll Post')
    parser.add_argument('title', help='The title of the post.')
    #parser.add_argument('category', help='The categores of the post.')
    parser.add_argument('--tag', help='The tags of the post.', default='blog')
    args = parser.parse_args()
    
    title = args.title
    categories = "" #args.category
    tags = "" #args.tag if args.tag else args.category

    name, date = time.strftime('%Y-%m-%d') + '-' + title.replace(' ','-') + '.md', time.strftime('%Y-%m-%d %H-%M-%S %z')

    path = "_posts/" + name

    yaml = '''---
layout: post
title: "%s"
date: %s
category: %s
tags: %s
---'''
    post = yaml % (title, date, categories, tags)
    fp = None
    try:
        fp = open(path, 'w')
        fp.write(post)
        print("It all worked out!")
    finally:
        if fp:
            fp.close()

if __name__ == '__main__':
    main()
