AUTHOR = 'Declan Gaylo'
SITENAME = 'Declan Gaylo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Setup URLS
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

# Theme setup
THEME = './pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Publications', '/publications.html'),
)

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (
#    ('Email', 'mailto:dgaylo@mit.edu', 'dgaylo@mit.edu'),
#    ("Github", "https://github.com/dgaylo/", "Elegant Github Repository"),
#)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
