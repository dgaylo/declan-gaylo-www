AUTHOR = 'Declan Gaylo'
SITENAME = 'Declan Gaylo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

COPY_DATE='20XX'

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

STATIC_PATHS = ['images','extra']
ARTICLE_PATHS  = ['posts']
PAGE_PATHS = ['pages']

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'sitemap', 'webassets', 'pelican.plugins.add_css_classes']

ADD_CSS_CLASSES = {}
ADD_CSS_CLASSES_TO_PAGE = {}
ADD_CSS_CLASSES_TO_ARTICLE = {
    "table": ["table table-striped table-sm"],
}

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
THEME = './mytheme'

# Bootstrap setup
BOOTSTRAP_CDN_CSS='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
BOOTSTRAP_CDN_CSS_INTEGRITY='sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN'
BOOTSTRAP_CDN_JS='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'
BOOTSTRAP_CDN_JS_INTEGRITY='sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL'

# Themes from http://bootswatch.com
BOOTSWATCH_THEME="cosmo"
BOOTSWATCH_CDN='https://cdn.jsdelivr.net/npm/bootswatch@5.3/dist/'+BOOTSWATCH_THEME.lower()+'/bootstrap.min.css'
THEME_COLOR='#F8F9FA'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
FONT_AWESOME_KIT = 'b3b7784092'
USE_WEBP = True

SOURCE_CODE_URL= 'https://github.com/dgaylo/declan-gaylo-www'

#CUSTOM_CSS = 'theme/custom.css'
WEBASSETS_SOURCE_PATHS = ['../content/', 'dynamic']
THEME_TEMPLATES_OVERRIDES = [ './content/theme/' ]

TYPOGRIFY = False

# If the author, category and tag collections are not needed,
DIRECT_TEMPLATES = ['index', 'archives']

# About me
AVATAR = 'images/avatar.JPEG'
AVATAR_WEBP = 'images/avatar.webp'
AVATAR_WIDTH = 1067
AVATAR_HEIGHT = 800
ABOUT_ME = """
A PhD student at MIT studying Hydrodynamics. 
Research interests are turbulent bubbly flow near the free surface. 
Work includes both theoretical models and new CFD tools.
"""

# Favicon
FAVICON = 'images/logo.svg'
SITELOGO = 'images/logo.svg'
SITELOGO_SIZE = '18px'

# Banner
BANNER = 'images/banner.jpeg'
BANNER_WEBP = 'images/banner.webp'
BANNER_SUBTITLE = 'Naval Architecture & Hydrodynamics'
BANNER_ALL_PAGES = False

# Nav bar
DISPLAY_PAGES_ON_MENU = False
DEFAULT_CATEGORY  = "Posts"
MENUITEMS = (
    ('Publications', 'publications'),
    ('Education', 'education'),
)

DISABLE_SIDEBAR_TITLE_ICONS = True
# Blogroll
LINKS_WIDGET_NAME = 'Links'
LINKS = (
    ('Vortical Flow Research Lab', 'https://www.mit.edu/~vfrl/'),
)

# Social widget
SOCIAL_WIDGET_NAME = 'Profiles'
SOCIAL = (
    ('Resume', '/files/Declan Gaylo - Resume.pdf', 'bi bi-file-earmark-pdf-fill'),
    ('LinkedIn', 'https://www.linkedin.com/in/declan-gaylo', 'bi bi-linkedin'),
    ('Google Scholar', 'https://scholar.google.com/citations?hl=en&user=kA9LJygAAAAJ', 'bi bi-google'),
    ('GitHub', 'https://github.com/dgaylo/', 'bi bi-github'),
)

DEFAULT_PAGINATION = False

# Cache settings using .htaccess files
EXTRA_PATH_METADATA = {
    'extra/htaccess/theme_css': {'path': 'theme/css/.htaccess'},
    'extra/htaccess/theme_js': {'path': 'theme/js/.htaccess'},
    'extra/htaccess/images': {'path': 'images/.htaccess'},
    'extra/htaccess/static': {'path': 'static/.htaccess'},
}

# Google Analytics
GOOGLE_GLOBAL_SITE_TAG = 'G-0SEL0G18LQ'
GOOGLE_VERIFICATIION_TAG = 'QUWwxfPE7bJsHk2xKt1srAdzcLBN26SwiIsGFBMgGGw'
GOGGLE_DEBUG_MODE = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
