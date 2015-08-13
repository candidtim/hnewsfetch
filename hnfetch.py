#!/usr/bin/env python3

'''
The MIT License (MIT)

Copyright (c) 2015 candidtim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''


import sys
import json
import codecs
import argparse
import random
from urllib.request import urlopen


STORY_TEMPLATE = """%(title)s [%(score)d]
%(url)s
https://news.ycombinator.com/item?id=%(id)d"""


def get_json(url):
    with urlopen(url) as response:
        reader = codecs.getreader('utf-8')
        return json.load(reader(response))


def stories_ids(stories_type):
    return get_json('https://hacker-news.firebaseio.com/v0/%(stories_type)sstories.json' % locals())


def get_story(story_id):
    return get_json('https://hacker-news.firebaseio.com/v0/item/%d.json' % story_id)


def main(args):
    ids = stories_ids(args.stories_type)
    selection_size = args.selection_size % len(ids)
    story_index = random.randint(0, selection_size-1)
    story_id = ids[story_index]
    story = get_story(story_id)
    print(STORY_TEMPLATE % story)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show Hacker News stories in terminal')
    parser.add_argument('-n', nargs=1, dest='selection_size', action='store', type=int, default=[10],
                        help='select from N top/newest stories')
    parser.add_argument('--newest', dest='stories_type', action='store_const', const='new', default='top',
                        help='show newest stories (default: show top stories)')
    args = parser.parse_args()
    args.selection_size = abs(args.selection_size[0])
    main(args)

