from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('dss.questions.views',
    url(r'', 'hello'),
    url(r'^hello/', 'hello'),
)

urlpatterns += patterns('',
    # url(r'^admin/', include(admin.site.urls)),
)
