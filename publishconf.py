import os
import sys
import git
import datetime
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://dgaylo.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Google Analytics
GOGGLE_DEBUG_MODE = False

# source code link (with hash)
sha = git.Repo(search_parent_directories=True).head.object.hexsha
SOURCE_CODE_URL= SOURCE_CODE_URL+'/tree/'+sha

# copy right date
COPY_DATE=datetime.date.today().strftime('%Y')