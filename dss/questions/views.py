# Create your views here.

from django.http import HttpResponse

def hello(request):
    name=request.GET.get('name')
    html = "Hello, World! (and "+name+")"
    return HttpResponse(html)
