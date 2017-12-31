#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from os import getcwd, path

# PELICAN_OPTS
AUTHOR = 'd$pid'
AUTHOR_REAL = 'Dayton Pidhirney'
SITENAME = 'potato.sh'
PATH     = 'content'
TIMEZONE = 'America/Edmonton'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = path.join(getcwd().strip("src"), "static")
DELETE_OUTPUT_DIRECTORY = True


# Blogroll
LINKS = (('Seekintoo', 'https://www.seekintoo.com'),)

# Social widget
SOCIAL = (('github', 'https://github.com/daytonpid'),
          ('twitter', 'https://twitter.com/d$pid'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME_OPTS
DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 0
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 0
CAPITALIZE_HEADINGS = True
LICENSE = {
    'cc_name':"by-sa",
    'hosted':False,
    'compact':True,
    'brief':False
}
