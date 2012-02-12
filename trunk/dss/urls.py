
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Cron enabled.                                                                                                              
#import django_cron
#django_cron.autodiscover()

urlpatterns = patterns('dss.questions.views',
    url(r'^$', 'questions'),
    url(r'^hello/', 'hello'),
    url(r'^questions/$', 'questions'),
    url(r'^questions/(?P<question_id>\d+)/$', 'detail'),
    url(r'^(?P<question_id>\d+)/results/$', 'results'),
    url(r'^questions/(?P<question_id>\d+)/answer/$', 'answer'),
)

urlpatterns += patterns('dss.auth.views',
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', 'register'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
