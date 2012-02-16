# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer, AnsweredQuestion
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
import time

# Stephen Lowry, Stephen Murphy
def hello(request):
    if request.user.is_authenticated():
        hello = "Hello "+request.user.username
    else:
        if "question" not in request.session:
            request.session["question"] = "why is thie broke?"
    return render_to_response('questions/hello.html', {'color': request.session["question"]}, context_instance=RequestContext(request))

def questions(request):
    latest_question_list = Question.objects.all()
    return render_to_response('questions/index.html', {'latest_question_list': latest_question_list}, context_instance=RequestContext(request))

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)

    if request.user.is_authenticated():
        pass
    elif q not in request.session:
        return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))
    else:
        return render_to_response('questions/detail.html', {'question': q, 'answered': request.session[q]}, context_instance=RequestContext(request))

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
        elif q not in request.session:
            request.session[q] = selected_answer
        #selected_answer.save()
        if next == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        elif next not in request.session:
            return render_to_response('questions/detail.html', {'question': next}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': next, 'answered': request.session[next]}, context_instance=RequestContext(request))

def results(request):
    #q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {}) #{'question': q})
