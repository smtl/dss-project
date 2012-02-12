# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
"""from signedcookies import utils"""
import time

#from guest.decorators import guest_allowed, login_required

# A guest user account will be automatically created for unauthenticated users who access this view.
#@guest_allowed
#def some_view(request):
#    ....

# A guest user, like an unauthenticated user, will be redirected to the login page.
#@login_required
#def some_other_view(request):
 #  ...

def hello(request, name="world"):
    if 'name' in request.GET and request.GET['name'] is not None:
    	hello = "Hello "+request.GET['name']+"!"
    else:
        hello = "Hello World!"
    return HttpResponse(hello)

def questions(request):
    latest_question_list = Question.objects.all()
    return render_to_response('questions/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))

def answer(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = q.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render_to_response('questions/detail.html', {
            'question':q,
            'error_message': "You didn't choose an answer",
            }, context_instance=RequestContext(request))
    else:
        selected_answer.save()
        #return HttpResponseRedirect(reverse('questions.views.results', kwargs={'object_id': q.id}))
        return HttpResponseRedirect(reverse('dss.questions.views.results', args=(q.id,)))

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {'question': q})

def index(req):

   # A secret non-empty string to sign the cookie
   secret = 'my_secret'

   # Pass the cookie class and the secret to get_cookies() 
   signed_cookies = Cookie.get_cookies(req, Cookie.SignedCookie, secret=secret)

   # Get the returned signed cookie
   returned_signed = signed_cookies.get('signed', None)
   
   # If the signed cookie exists 
   if returned_signed:
      # Check if the cookie was not altered
      if type(returned_signed) is not Cookie.SignedCookie:
         message = 'The cookie was altered'
      else:
         message = 'The cookie was not altered'
   else:
      message = 'This is your first visit'
      
   # Create a signed cookie
   send_signed = Cookie.SignedCookie('signed', 'this string is signed', secret)

   # The cookie will expire in 30 days.
   send_signed.expires = time.time() + 30 * 24 * 60 * 60
   
   # Add the cookie to the HTTP header.
   Cookie.add_cookie(req, send_signed)

   return """\
<html><body>
<p>%s</p>
<p><pre>%s</pre></p>
<p>%s</p>
</body></html>
""" % ('You have just received this cookie:', send_signed, message)
