from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


#welcome page
def welcome(request):
    return render_to_response("welcome/welcome.html",{},context_instance=RequestContext(request))
