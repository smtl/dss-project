# Create your views here.

from django.http import HttpResponse

def hello(request):
    hello = "Hello "+request.GET['name']
    return HttpResponse(hello)
