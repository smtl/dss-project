from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core import cache
from django.http import HttpResponseRedirect, HttpResponse
from dss.questions.models import Question, Answer, AnsweredQuestion, QuestionPath
from dss.auth.models import UserProfile, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
import datetime
from django.core import cache
import hashlib
from django.core.urlresolvers import reverse

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def get_next_question_or_none(current_user):
    i = 0
    try:
        for i in xrange(Question.objects.count()):
            q = QuestionPath.objects.filter(profile=current_user.get_profile().profile)[i].current_question
            a = get_or_none(AnsweredQuestion, user=current_user,question=q)
            if a == None:
                return q
    except IndexError:
        # If the list has gone out of bounds go back and get the last question
        # Check if already answered
        if i > 1:
            q = QuestionPath.objects.filter(profile=current_user.get_profile().profile)[i-1].follow_question
        else:
            q = QuestionPath.objects.filter(profile=current_user.get_profile().profile)[0].follow_question
        a = get_or_none(AnsweredQuestion, user=current_user, question=q)
        if a == None:
            return q

    if i == Question.objects.count() or i > Question.objects.count():
            return None

def get_next_question_or_none_guest(request):
    i = 0
    p = get_or_none(Profile, name="Default")
    try:
        for i in xrange(Question.objects.count()):
            q = QuestionPath.objects.filter(profile=p)[i].current_question
            # have they answered it already?
            if q not in request.session:
                return q
    except IndexError:
        q = QuestionPath.objects.filter(profile=p)[i-1].follow_question
        if q not in request.session:
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
    # Guest user
    else:
        q = get_next_question_or_none_guest(request)
        if q == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': q}, context_instance=RequestContext(request))



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
        nextq = qpath.follow_question
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
            answered = get_or_none(AnsweredQuestion, user=request.user, question=q)
            if answered == None:
                qa = AnsweredQuestion()
                qa.user = request.user
                qa.answer = selected_answer
                qa.question = q
                qa.save()
            else:
                answered.answer = selected_answer
                answered.save()
        elif q not in request.session:
 	        request.session[q] = selected_answer
        else:
            # Delete the old answer before adding the new one
            del request.session[q]
            request.session[q] = selected_answer
        
        if qpath == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': nextq}, context_instance=RequestContext(request))


def results(request):
    #q = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))



# Lets a user change the answer they gave
def edit(request, input_id):
    # If a new answer is submitted
    if request.method == 'POST':
        # Find the question
        q = get_or_none(Question, pk=input_id)

        try:
            # Make sure they have selected an answer
            selected_answer = q.answer_set.get(pk=request.POST['answer'])
        except (KeyError, Answer.DoesNotExist):
            return render_to_response('questions/edit.html', { 'question':q, 'error_message': "You didn't choose an answer",}, context_instance=RequestContext(request))
        else: 
            if request.user.is_authenticated():
                # Find the old answer
                qa = get_or_none(AnsweredQuestion, user=request.user, question=input_id)
                if qa != None:
                    # Edit the old answer
                    qa.answer_id = request.POST['answer']
                    qa.save()
                return HttpResponseRedirect(reverse("profile"))
            else:   
                if q in request.session:
                    # Delete the old answer before adding the new one
                    del request.session[q]
                    request.session[q] = selected_answer
    
                return HttpResponseRedirect(reverse("profile"))
    # Get the question to show
    else:
        if request.user.is_authenticated():
            q = get_or_none(Question, pk=input_id)
        else:
            answer = get_or_none(Answer, pk=input_id)
            if answer != None:
                q = get_or_none(Question, pk=answer.question_id)

        return render_to_response('questions/edit.html', {'question': q}, context_instance=RequestContext(request))


def save_progress(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()   
            # Give them a profile
            up = UserProfile()
            up.user_id = new_user.id
            up.profile_id = 1
            up.save()   
            # Transfer their answered questions from guest session to user account
            for q in Question.objects.all():
                if q in request.session:
                    AnsweredQuestion.objects.create(user=new_user, question=q, answer=request.session[q])
            return HttpResponseRedirect(reverse("login"))
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form}, context_instance=RequestContext(request))


#Adrian Kwizera
def record_view(request):
    count = User.objects.count()
    return render_to_response('questions/record_view.html', {'count': count}, context_instance=RequestContext(request))




#viewing user info by admin and maintainer for specification purposes
def get_user_info(username):
    c = cache.get_cache('default')
    username = unicode(username).encode('ascii', 'ignore')
    key = 'trac_user_info:%s' % hashlib.md5(username).hexdigest()
    info = c.get(key)
    if info is None:
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            info = {"core": False, "cla": False}
        else:
            info = {
                "core": u.has_perm('auth.commit'),
                "cla": bool(find_agreements(u))
            }
        c.set(key, info, 60*60)
    return info

def help(request):
    if request.user.is_staff:
        return render_to_response('questions/help_staff.html', {}, context_instance=RequestContext(request))
    else:
        return render_to_response('questions/help_user.html', {}, context_instance=RequestContext(request))
