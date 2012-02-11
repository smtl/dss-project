
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Cron enabled.                                                                                                              
#import django_cron
#django_cron.autodiscover()

urlpatterns = patterns('dss.questions.views',
    url(r'^$', 'hello'),
    url(r'^hello/', 'hello'),
    url(r'^questions/$', 'questions'),
    url(r'^questions/(?P<question_id>\d+)/$', 'detail'),
    url(r'^(?P<question_id>\d+)/results/$', 'results'),
    url(r'^questions/(?P<question_id>\d+)/answer/$', 'answer'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
