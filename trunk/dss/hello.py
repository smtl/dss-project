from django.http import HttpResponse
import settings
import os

def hello(request):
    response = HttpResponse()
    response.write("<h1>Hello world!</h1>\n")
    response.write("<ul>\n")
    response.write("<li>My DJANGO_ROOT is '" + settings.DJANGO_ROOT + "'</li>\n")
    response.write("<li>My SITE_ROOT is '" + settings.SITE_ROOT + "'</li>\n")
    response.write("<li>My DATABASE_NAME is '" + settings.DATABASE_NAME + "'</li>\n")
    response.write("<li>My WSGI REQUEST_URI is '" + request.META['REQUEST_URI']  + "'</li>\n")
    response.write("<li>My WSGI script dir is '" + os.path.dirname(request.META['SCRIPT_NAME'])  + "'</li>\n")
    response.write("<li>My WSGI SCRIPT_NAME is '" + request.META['SCRIPT_NAME']  + "'</li>\n")
    response.write("<li>My WSGI DOCUMENT_ROOT is '" + request.META['DOCUMENT_ROOT']  + "'</li>\n")
    response.write("<li>My WSGI SERVER_NAME is '" + request.META['SERVER_NAME']  + "'</li>\n")
#    os.environ['WSGI_SCRIPT_DIR'] = os.path.dirname(environ['SCRIPT_NAME'])
    response.write("</ul>\n")
    response.write("<p>You can access a <a href='" + os.path.dirname(request.META['SCRIPT_NAME']) + "/static/index.html'>file</a> in my <em>static</em> directory.")
    return response
