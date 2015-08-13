#!/usr/bin/env python3

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
