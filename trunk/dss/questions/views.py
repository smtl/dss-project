# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext

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
