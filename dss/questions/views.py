# Create your views here.

from django.http import HttpResponse

def hello(request, name="world"):
    if 'name' in request.GET and request.GET['name'] is not None:
    	hello = "Hello "+request.GET['name']+"!"
    else:
        hello = "Hello World!"
    return HttpResponse(hello)
