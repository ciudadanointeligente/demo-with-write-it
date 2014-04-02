from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
#Writeit specific urls
urlpatterns += patterns('',
                        url(r'^', include('nuntium.urls')),
                        url(r'^', include('nuntium.user_section.urls')),
                        (r'accounts/', include('django.contrib.auth.urls')),
                             )
