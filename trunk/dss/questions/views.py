# Create your views here.
# test comment

from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer, AnsweredQuestion, QuestionPath
from dss.auth.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
import datetime

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def hello(request, name="world"):
    if request.user.is_authenticated():
        hello = "Hello "+request.user.username
    else:
        hello = "Hello stranger"
    return HttpResponse(hello)

# Show a list of questions
def questions(request):
    latest_question_list = Question.objects.all()
    return render_to_response('questions/index.html', {'latest_question_list': latest_question_list}, context_instance=RequestContext(request))

# Present the question to the user
def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    #return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))
    
    # Check if user is logged in
    if request.user.is_authenticated():
        answered_already = get_or_none(AnsweredQuestion, user=request.user, question=q)
        # Check if they have already answered this question
        if answered_already == None:
            return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': q, 'answered': answered_already.answer}, context_instance=RequestContext(request))
    # or check if they are a guest that has already answered this question
    elif q not in request.session:
        return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))
    else:
        return render_to_response('questions/detail.html', {'question': q, 'answered': request.session[q]}, context_instance=RequestContext(request))

# Handles the answer selected by the user/guest
def answer(request, question_id):
    q = get_or_none(Question, pk=question_id)
    #num = int(question_id)+1
    # Get the next question for the user based on the profile path set for their profile type
    if request.user.is_authenticated():
        up = UserProfile.objects.get(user=request.user)
        qpath = get_or_none(QuestionPath, current_question=q, profile=request.user.get_profile().profile)
        #qpath = QuestionPath.objects.get(current_question=q,profile=up.id) 
    else:
        qpath = get_or_none(QuestionPath, current_question=q, profile=1)
    if qpath != None:
        next = qpath.follow_question
    else:
        return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
    try:
        # Make sure they have selected an answer
        selected_answer = q.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render_to_response('questions/detail.html', {
            'question':q,
            'error_message': "You didn't choose an answer",
            }, context_instance=RequestContext(request))
    else:
        # Save their answer if they are logged in
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
            return render_to_response('questions/results.html')
        else:
            return render_to_response('questions/detail.html', {'question': next})

def results(request):
    #q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {}) #{'question': q})

#Adrian Kwizera
def record_view(request):
    count = User.objects.count()
    return render_to_response('questions/record_view.html', {'count': count})

