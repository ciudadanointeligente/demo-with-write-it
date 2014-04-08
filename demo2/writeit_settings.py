MIDDLEWARE_CLASSES = (
        'subdomains.middleware.SubdomainURLRoutingMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
EXTRA_APPS = (
    'nuntium',
    'contactos',
    'mailit',
    'django.contrib.sites',
    'south',
    'popit',
    'markdown_deux',
    'subdomains',
    'djangoplugins',
    'tastypie',
)
NEW_ANSWER_DEFAULT_SUBJECT_TEMPLATE = ''
SITE_ID=1
ROOT_URLCONF = 'nuntium.subdomain_urls'
HAYSTACK_CONNECTIONS = {
    'default': {
                    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                    'URL': 'http://127.0.0.1:9200/',
                    'INDEX_NAME': 'demo2',
                },
    }
SUBDOMAIN_URLCONFS = {
        None: 'demo2.urls',
}
