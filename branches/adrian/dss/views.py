# Create your views here.

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world.")

def other_func(request):
    return HttpResponse("Not found.")

