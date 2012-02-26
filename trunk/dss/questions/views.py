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

def get_next_question_or_none(current_user):
    for i in xrange(Question.objects.count()-2):
        q = QuestionPath.objects.filter(profile=current_user.get_profile().profile)[i].current_question
        a = get_or_none(AnsweredQuestion, user=current_user,question=q)
        if a == None:
            return q

    if i == Question.objects.count() or i > Question.objects.count():
        return None




def hello(request, name="world"):
    if request.user.is_authenticated():
        hello = "Hello "+request.user.username
    else:
        hello = "Hello stranger"
    return HttpResponse(hello)



# Show a list of questions
def index(request):
    if request.user.is_authenticated():
        # If the user 
        q = get_next_question_or_none(request.user)
        if q == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))
    else:
        latest_question_list = Question.objects.all()
        return render_to_response('questions/index.html', {'latest_question_list': latest_question_list}, context_instance=RequestContext(request))

def questions(request):
    if request.user.is_authenticated():
        answered = AnsweredQuestion.objects.filter(user=request.user)
        return render_to_response('questions/answered_questions.html', {'answered_questions': answered}, context_instance=RequestContext(request))
    else:
        answered = []
        for q in Question.objects.all():
            if q in request.session:
                answered.append(request.session[q])
        return render_to_response('questions/answered_questions.html', {'answered_questions': answered}, context_instance=RequestContext(request))



# Present the question to the user
def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    
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
    # Get the next question for the user based on the profile path set for their profile type
    if request.user.is_authenticated():
        up = UserProfile.objects.get(user=request.user)
        qpath = get_or_none(QuestionPath, current_question=q, profile=request.user.get_profile().profile)
    else:
        qpath = get_or_none(QuestionPath, current_question=q, profile=1)
    if qpath != None:
        next = qpath.follow_question
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
        if qpath == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': next}, context_instance=RequestContext(request))


def results(request):
    #q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))


# Lets a user change the answer they gave
def edit(request, question_id):
    if request.method == 'POST':
        qa = get_or_none(AnsweredQuestion, user=request.user, question=question_id)
        if qa != None:
            qa.answer_id = request.POST['answer']
            qa.save()
        return HttpResponseRedirect("/questions")
    else:    
        q = get_or_none(Question, pk=question_id)
        return render_to_response('questions/edit.html', {'question': q}, context_instance=RequestContext(request))


#Adrian Kwizera
def record_view(request):
    count = User.objects.count()
    return render_to_response('questions/record_view.html', {'count': count})
