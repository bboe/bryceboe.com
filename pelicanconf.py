#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = 'Bryce Boe'
SITENAME = 'Bryce Boe'
SITEURL = ''
SITESUBTITLE = 'The Adventures of a UCSB Computer Science Ph.D. Student'

# Site paths / urls
ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'

# General Settings
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
PLUGINS = ['pelican_gist', 'plugins.related_posts', 'plugins.sitemap']
TAG_CLOUD_MAX_ITEMS = 10
THEME = 'themes/pelican-bootstrap3'
TIMEZONE = 'America/Los_Angeles'
TYPOGRIFY = True

# Disable pages
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Adam Doupé', 'http://adamdoupe.com/'),
         ('Julie Bifano', 'http://juliebifano.com/'))

# Social widget
SOCIAL = (('github', 'https://github.com/bboe'),
          ('stack-overflow', 'http://stackoverflow.com/users/176978/bboe'),
          ('linkedin', 'http://www.linkedin.com/in/bbzbryce'),
          ('google+', 'https://plus.google.com/+BryceBoe?rel=author'),
          ('twitter', 'https://twitter.com/bboe'))

# Static files (.htaccess, robots.txt)
STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt', 'images']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'}}

# Sitemap
SITEMAP = {'format': 'xml',
           'priorities': {'articles': 1, 'indexes': 0.25, 'pages': 0.5},
           'changefreqs': {'articles': 'monthly', 'indexes': 'daily',
                           'pages': 'monthly'}}

# pelican-bootstrap3 settings
#ADDTHIS_PROFILE = 'ra-52ea977465521a04'
BOOTSTRAP_THEME = 'cerulean'
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISQUS_NO_ID = True
PYGMENTS_STYLE = 'solarizedlight'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
