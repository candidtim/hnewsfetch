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


# load and use urllib3 if it is available, fallback to urllib otherwise
try:
    import urllib3
    UrlOpenError = urllib3.exceptions.HTTPError
    use_urllib3 = True
except ImportError:
    import urllib
    UrlOpenError = urllib.error.URLError
    use_urllib3 = False


API_BASE_URL = 'https://hacker-news.firebaseio.com'
RESPONSE_ENCODING = 'utf-8'

STORY_TEMPLATE = """%(title)s [%(score)d]
%(url)s
https://news.ycombinator.com/item?id=%(id)d"""


if use_urllib3:
    connection = urllib3.connection_from_url(API_BASE_URL, timeout=1.0)
    def get_json(request_path):
        response = connection.request('GET', request_path)
        return json.loads(response.data.decode(RESPONSE_ENCODING))
else:
    def get_json(request_path):
        with urllib.request.urlopen(API_BASE_URL + request_path, timeout=1.0) as response:
            reader = codecs.getreader(RESPONSE_ENCODING)
            return json.load(reader(response))


def stories_ids(stories_type):
    return get_json('/v0/%(stories_type)sstories.json' % locals())

def get_story(story_id):
    return get_json('/v0/item/%d.json' % story_id)


def main(args):
    try:
        ids = stories_ids(args.stories_type)
        selection_size = args.selection_size % len(ids)
        story_index = random.randint(0, selection_size-1)
        story_id = ids[story_index]
        story = get_story(story_id)
    except UrlOpenError:
        print('Cannot connect to %s' % API_BASE_URL)
    else:
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

