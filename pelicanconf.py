#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Louie Dinh'
SITENAME = 'Quantiative Rhetoric'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/louiedinh'),
          ('linkedin', 'https://linkedin.com/in/louiedinh'),
          ('github', 'https://github.com/louiedinh'))

DEFAULT_PAGINATION = False

THEME = 'themes/pelican-blue'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'notes', 'notebooks', 'static']
ARTICLE_EXCLUDES = ['notebooks', 'static']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
