#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bryce Boe'
SITENAME = 'Bryce Boe'
SITEURL = ''

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

PLUGINS = ['plugins.sitemap']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Robots.txt
STATIC_PATHS = ['extra/robots.txt', 'images']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'}}

# Sitemap
SITEMAP = {'format': 'xml',
           'priorities': {'articles': 1, 'indexes': 0.25, 'pages': 0.5},
           'changefreqs': {'articles': 'monthly', 'indexes': 'daily',
                           'pages': 'monthly'}}



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
