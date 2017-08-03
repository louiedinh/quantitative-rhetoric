#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Louie Dinh'
SITENAME = 'Quantitative Rhetoric'
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
LINKS = (('Better Dwelling', 'https://betterdwelling.com/'),
        ('Vancouver Condo Info', 'http://vancouvercondo.info/'),
        ('Mountain Doodles', 'http://doodles.mountainmath.ca/'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/louiedinh'),
          ('linkedin', 'https://linkedin.com/in/louiedinh'),
          ('github', 'https://github.com/louiedinh'))

DEFAULT_PAGINATION = False

THEME = 'themes/pelican-blue'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'notes', 'notebooks', 'static']
ARTICLE_EXCLUDES = ['notebooks', 'static', 'drafts']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Needs to go here because of the way we generate the signup
GOOGLE_ANALYTICS = 'UA-39716444-3'
