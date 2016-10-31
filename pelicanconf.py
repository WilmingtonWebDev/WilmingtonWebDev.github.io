#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Marks'
SITENAME = u'Wilmington Web Dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

THEME = 'themes/html5-dopetrope'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

# Blogroll
LINKS = (
    ('TheMillSpace', 'http://themillspace.com/'),
    ('Kurbi', 'http://gokurbi.com/')
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#')
)

DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('Home', '/'),
    ('MeetUps', '/meetups.html'),
    ('About', '/about.html'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_METADATA = {
    'status': 'draft',
}

TWITTER_USER = 'ThomasMarks'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
