import os
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# Cron enabled.                                                                                                              
#import django_cron
#django_cron.autodiscover()

# from a stackoverflow q http://stackoverflow.com/questions/5152026/django-admin-media-prefix-url-issue
def fromRelativePath(*relativeComponents):
    return os.path.join(os.path.dirname(__file__), *relativeComponents).replace("\\","/")

urlpatterns = patterns('dss.questions.views',
    url(r'^$', 'index', name='index'),
    url(r'^hello/$', 'hello'),
    url(r'^questions/$', 'questions'),
    url(r'^questions/(?P<question_id>\d+)/$', 'detail', name='detail'),
    url(r'^questions/results/$', 'results', name='results'),
    url(r'^questions/(?P<question_id>\d+)/answer/$', 'answer', name='answer'),
    url(r'^questions/(?P<input_id>\d+)/edit/$', 'edit', name='edit'),
    url(r'^save/$', 'save_progress', name='save_progress'),
    url(r'^help/$', 'help', name='help'),
)

urlpatterns += patterns('dss.auth.views',
    url(r'^accounts/login/$', login, name='login'),
    #url(r'^accounts/logout/$', logout),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', 'register', name='register'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'changeprofile/$', 'change_profile', name='changeprofile'),
)

urlpatterns += patterns('dss.recommendations.views',
    url(r'^recommendations/$', 'show'),
)

urlpatterns += patterns('',
    url(r"^admin/recommendations/uploadedfile/$","handle_uploaded_file"),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    #url("^admin_media/(?P<path>.*)$", "django.views.static.serve",{ "document_root": fromRelativePath("static", "admin") }),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

