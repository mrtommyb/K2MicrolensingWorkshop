#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Barclay'
SITENAME = u'K2 Microlensing Workshop'
SITEURL = ''

THEME = "/Users/tom/websites/K2MicrolensingWorkshop/tom-theme/gum"

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

TYPOGRIFY = True

PATH = 'content'

PAGE_ORDER_BY = 'pageorder'
ARTICLE_ORDER_BY = 'sortorder'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Workshop', '/index.html'),
    ('Venue', '/venue'),
    ('Agenda', '/agenda'),
    ('Call-in Information', '/callin'),
)

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
