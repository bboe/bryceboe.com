#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = 'Bryce Boe'
SITENAME = 'Bryce Boe'
SITEURL = ''
SITESUBTITLE = 'The Adventures of a UCSB Computer Science Ph.D. Student'
TWITTER_USERNAME = 'bboe'

# Site paths / urls
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

# General Settings
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
PLUGINS = ['plugins.sitemap', 'pelican_gist']
TIMEZONE = 'America/Los_Angeles'
TYPOGRIFY = True

# Disable pages
ARCHIVES_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
TAGS_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Adam Doupé', 'http://adamdoupe.com/'),
         ('Julie Bifano', 'http://juliebifano.com/'))

# Social widget
SOCIAL = (('+BryceBoe', 'https://plus.google.com/+BryceBoe'),
          ('@bboe', 'https://twitter.com/bboe'),
          ('bboe', 'https://github.com/bboe'),
          ('bbzbryce', 'http://www.last.fm/user/bbzbryce'),
          ('/u/bboe', 'http://www.reddit.com/user/bboe'))

# Static files (.htaccess, robots.txt)
STATIC_PATHS = ['extra/robots.txt', 'images']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'}}

# Sitemap
SITEMAP = {'format': 'xml',
           'priorities': {'articles': 1, 'indexes': 0.25, 'pages': 0.5},
           'changefreqs': {'articles': 'monthly', 'indexes': 'daily',
                           'pages': 'monthly'}}



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
