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
from urllib.request import urlopen


STORY_TEMPLATE = """%(title)s [%(score)d]
%(url)s
https://news.ycombinator.com/item?id=%(id)d"""


def get_json(url):
    with urlopen(url) as response:
        reader = codecs.getreader('utf-8')
        return json.load(reader(response))


def top_stories_ids():
    return get_json('https://hacker-news.firebaseio.com/v0/topstories.json')


def get_story(story_id):
    return get_json('https://hacker-news.firebaseio.com/v0/item/%d.json' % story_id)


def main():
    top_story_id = top_stories_ids()[0]
    top_story = get_story(top_story_id)
    print(STORY_TEMPLATE % top_story)


if __name__ == "__main__":
    main()
