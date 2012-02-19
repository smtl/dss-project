
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Cron enabled.                                                                                                              
#import django_cron
#django_cron.autodiscover()

urlpatterns = patterns('dss.questions.views',
    url(r'^$', 'index'),
    url(r'^hello/$', 'hello'),
    url(r'^questions/$', 'questions'),
    url(r'^questions/(?P<question_id>\d+)/$', 'detail'),
    url(r'^questions/results/$', 'results'),
    url(r'^questions/(?P<question_id>\d+)/answer/$', 'answer'),
    url(r'^record_view/$', 'record_view'),
   
)

urlpatterns += patterns('dss.auth.views',
    url(r'^accounts/login/$', login),
    #url(r'^accounts/logout/$', logout),
    url(r'^accounts/logout/$', logout,
                          {'next_page': '/'}),
    url(r'^accounts/register/$', 'register'),
    url(r'^profile/$', 'profile'),
    url(r'changeprofile/$', 'change_profile'),
)

urlpatterns += patterns('dss.recommendations.views',
    url(r'^recommendations/$', 'show'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
