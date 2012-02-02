from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns += staticfiles_urlpatterns()

urlpatterns = patterns('wordconfuse.views',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # url(r'^admin/', include(admin.site.urls)),
        (r'^$', 
TemplateView.as_view(template_name="index.html")),
        url(r'^get_words$', 'get_words', name='get_words'),
        url(r'^gameover$', 'gameover', name='gameover'),
        url(r'^new_hs$', 'new_hs', name='new_hs'),
        url(r'^hs$', 'hs', name='hs'),
)
