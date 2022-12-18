AUTHOR = 'Declan Gaylo'
SITENAME = 'Declan Gaylo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

GOOGLE_GLOBAL_SITE_TAG = 'G-0SEL0G18LQ'
GOOGLE_VERIFICATIION_TAG = 'QUWwxfPE7bJsHk2xKt1srAdzcLBN26SwiIsGFBMgGGw'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Setup URLS
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS  = '{slug}/index.html'
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# Defualts not to generate
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

STATIC_PATHS = ['images','static','extra']
ARTICLE_PATHS  = ['posts']
PAGE_PATHS = ['pages']

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'sitemap', 'webassets']

# Sitemap
SITEMAP = {
    "format": "xml",
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    },
    "exclude": ["index"]
}

# Theme setup
THEME = './pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
FONT_AWESOME_KIT = 'b3b7784092'
DISPLAY_ARTICLE_LIST_ON_INDEX = False
USE_WEBP = True

SOURCE_CODE_URL= 'https://github.com/dgaylo/declan-gaylo-www'

CUSTOM_CSS = 'static/custom.css'
WEBASSETS_SOURCE_PATHS = ['../../content/']

THEME_TEMPLATES_OVERRIDES = [ './content/theme/' ]

TYPOGRIFY = False

# If the author, category and tag collections are not needed,
DIRECT_TEMPLATES = ['index', 'archives']

# About me
AVATAR = 'images/avatar.JPEG'
AVATAR_WEBP = 'images/avatar.webp'
ABOUT_ME = """
I’m currently a PhD student at MIT studying Hydrodynamics. 
My research interests are turbulent bubbly flow near the free surface. 
My work includes both theoretical models and new CFD tools.
"""

# Favicon
FAVICON = 'images/logo.svg'
SITELOGO = 'images/logo.svg'
SITELOGO_SIZE = '18px'
SITELOGO_ALT = 'Site Logo'

# Banner
BANNER = 'images/banner.jpeg'
BANNER_WEBP = 'images/banner.webp'
BANNER_SUBTITLE = 'Naval Architecture & Hydrodynamics'
BANNER_ALL_PAGES = True

# Nav bar
DISPLAY_PAGES_ON_MENU = False
DEFAULT_CATEGORY  = "Posts"
MENUITEMS = (
    ('Publications', 'publications'),
    ('Education', 'education'),
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

# Cache settings using .htaccess files
EXTRA_PATH_METADATA = {
    'extra/htaccess/theme_css': {'path': 'theme/css/.htaccess'},
    'extra/htaccess/theme_js': {'path': 'theme/js/.htaccess'},
    'extra/htaccess/images': {'path': 'images/.htaccess'},
    'extra/htaccess/static': {'path': 'static/.htaccess'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
