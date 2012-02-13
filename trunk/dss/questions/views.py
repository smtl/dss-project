# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer, AnsweredQuestion
from django.contrib.auth.models import User
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
    if request.user.is_authenticated():
        hello = "Hello "+request.user.username
    else:
        hello = "Hello stranger"
    return HttpResponse(hello)

def questions(request):
    latest_question_list = Question.objects.all()
    return render_to_response('questions/index.html', {'latest_question_list': latest_question_list}, context_instance=RequestContext(request))

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def answer(request, question_id):
    q = get_or_none(Question, pk=question_id)
    num = int(question_id)+1
    next = get_or_none(Question, pk=num)
    try:
        selected_answer = q.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render_to_response('questions/detail.html', {
            'question':q,
            'error_message': "You didn't choose an answer",
            }, context_instance=RequestContext(request))
    else:
        if request.user.is_authenticated():
            qa = AnsweredQuestion()
            qa.user = request.user
            qa.answer = selected_answer
            qa.question = q
            qa.save()
        #selected_answer.save()
        if next == None:
            return render_to_response('questions/results.html')
        else:
            return render_to_response('questions/detail.html', {'question': next})

def results(request):
    #q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {}) #{'question': q})
