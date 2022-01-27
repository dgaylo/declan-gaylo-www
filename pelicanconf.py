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

STATIC_PATHS = ['images', 'files', 'extra']

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

# Theme setup
THEME = './pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
FONT_AWESOME_KIT = 'b3b7784092'

CUSTOM_CSS = 'static/css/custom.css'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}

# About me
AVATAR = 'images/avatar.jpeg'
ABOUT_ME = """
I\'m a Naval Architect working tword my PhD in Hydrodynamcis at MIT. 
My reseach interests are the complex interactions between turubelnce and the free surface, 
and I develop both theoretical models and new CFD codes.
Before MIT I attended Webb Instutue, where I learned of and experinced the broad range of the marine industry.
"""


# Banner
BANNER = 'images/banner.jpeg'
BANNER_SUBTITLE = 'Naval Architecture & Hydrodynamics'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Publications', '/publications.html'),
)

DISABLE_SIDEBAR_TITLE_ICONS = True
# Blogroll
LINKS = (
    ('Vortical Flow Research Lab', 'https://www.mit.edu/~vfrl/'),
)

# Social widget
SOCIAL_WIDGET_NAME = 'Profiles'
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/declan-gaylo', 'fab fa-linkedin'),
    ('Google Scholar', 'https://scholar.google.com/citations?hl=en&user=kA9LJygAAAAJ', 'fab fa-google'),
    ('ORCiD', 'https://orcid.org/0000-0001-6198-7003', 'fab fa-orcid'),
    ('GitHub', 'https://github.com/dgaylo/'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
