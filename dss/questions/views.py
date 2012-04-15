from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core import cache
from django.http import HttpResponseRedirect, HttpResponse
from questions.models import Question, Answer, AnsweredQuestion, QuestionPath
from recommendations.models import Recommendation, UserRecommendation
from auth.models import UserProfile, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
import datetime
from django.core import cache
import hashlib
from django.core.urlresolvers import reverse
import os
import re

#def parse_rule(rule, request):
#    # rule is a string
#    # "if 2 or 3 and 5 then r7"
#    bool_rule = re.compile(":").split(rule)[0]
#    result_part = re.compile(":").split(rule)[1]
#    print "This is the bool_rule: "+bool_rule
#    tokens = bool_rule.split(' ')
#    result_tokens = result_part.split(' ')
#    new_rule = bool_rule
#    current_user = request.user
#    # create the logic string
#    for t in tokens:
#        if 'ans' in t:
#            current_answer = get_or_none(Answer, id=int(float(t[3:]))
#            # Handle users and guests differently
#            if current_user.is_authenticated():
#                ans_bool_result = get_or_none(AnsweredQuestion, user=current_user, answer=current_answer)
#            elif current_answer.question in request.session:
#                ans_bool_result = "question found"
#            else:
#                ans_bool_result = None
#
#            if ans_bool_result == None:
#                ans_bool = False
#            else:
#                ans_bool = True
#            # create the new rule which is to be executed
#            new_rule = new_rule.replace(t, str(ans_bool))
#    
#    # Build and execute the rule putting the result in the "result" variable
#    result_string = "result = "+new_rule
#    exec(result_string)
#    if result == True:
#        # Actions for the outcomes of a rule
#        for t in result_tokens:
#            # red denotes redundancy
#            if "red" in t:
#                print "outcome results in a question being made redundant"
#                question = get_or_none(Question, id=int(float(t[3:])))
#                # check if question has already been answered, if it has there is no point marking it redundant
#                # actually this is a design decision - it can be changed if neccesary
#                if current_user.is_authenticated():
#                    answered = get_or_none(AnsweredQuestion, user=current_user, question=question)
#                elif question in request.session:
#                    answered = "question found"
#                else:
#                    answered = None
#
#                if answered == None:
#                    if current_user.is_authenticated():
#                        aq = AnsweredQuestion()
#                        aq.user = current_user
#                        aq.question = question
#                        aq.answer_id = 0
#                        aq.redundancy = 1
#                        aq.save()
#                    else:
#                        # redundancy marked by r at the start of the question
#                        request.session["r"+question] = 0
#            # rec denotes recommendation
#            elif "rec" in t:
#                print "outcome results in a recommendation being recommended"
#                rec = get_or_none(Recommendation, id=int(float(t[3:])))
#                # check if recommendation is already recommended for user or guest
#                if current_user.is_authenticated():
#                    recommended = get_or_none(UserRecommendation, user=current_user, recommendation=rec)
#                elif rec in request.session:
#                    recommended = request.session[rec]
#                if recommended == None:
#                    if current_user.is_authenticated():
#                        ur = UserRecommendation()
#                        ur.user = current_user
#                        ur.recommendation = rec
#                        ur.save()
#                    else:
#                        request.session[rec] = rec
#            # answer denotes to answer a question implictly
#            elif "ans" in t:
#                print "outcome results in marking a answer as implicitly answered"
#                # check if question is already answered by user. If it is, there is no need to mark it implicit
#                answer = get_or_none(Answer, id=int(float(t[3:])))
#                if current_user.is_authenticated():
#                    answered = get_or_none(AnsweredQuestion, user=current_user, question=answer.question)
#                elif answer.question in request.session:
#                    answered = "Not None"
#                else:
#                    answered = None
#
#                if answered == None:
#                    if current_user.is_authenticated():
#                        aq = AnsweredQuestion()
#                        aq.user = current_user
#                        aq.question = answer.question
#                        aq.answer = answer
#                        aq.implicit = 1
#                        aq.save()
#                    else:
#                        request.session["i"+answer.question] = answer
#    else:
#        print "false lol"

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

# Gets next question in queue or none in case the current user saves state or exits
def get_next_question_or_none(current_user):
    i = 0
    try:
        for i in xrange(Question.objects.count()):
            try:
                p = UserProfile.objects.get(user=current_user)
            except UserProfile.DoesNotExist:
                up = UserProfile()
                up.user = current_user
                up.profile_id = 1
                up.save()
                p = UserProfile.objects.get(user=current_user)

            q = QuestionPath.objects.filter(profile=current_user.get_profile().profile)[i].current_question 
            # if the question isn't found then it hasn't been answered so it can be returned
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

# Similar as above, but for guests this time
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

def get_script_name(request):
    return request.META['SCRIPT_NAME']

# hello request
def hello(request):
    response = HttpResponse()
    response.write("<h1>Hello world!</h1>\n")
    response.write("<ul>\n")
    response.write("<li>My DJANGO_ROOT is '" + settings.DJANGO_ROOT + "'</li>\n")
    response.write("<li>My SITE_ROOT is '" + settings.SITE_ROOT + "'</li>\n")
    response.write("<li>My DATABASE_NAME is '" + settings.DATABASE_NAME + "'</li>\n")
    response.write("<li>My WSGI REQUEST_URI is '" + request.META['REQUEST_URI']  + "'</li>\n")
    response.write("<li>My WSGI script dir is '" + os.path.dirname(request.META['SCRIPT_NAME'])  + "'</li>\n")
    response.write("<li>My WSGI SCRIPT_NAME is '" + request.META['SCRIPT_NAME']  + "'</li>\n")
    response.write("<li>My WSGI DOCUMENT_ROOT is '" + request.META['DOCUMENT_ROOT']  + "'</li>\n")
    response.write("<li>My WSGI SERVER_NAME is '" + request.META['SERVER_NAME']  + "'</li>\n")
#    os.environ['WSGI_SCRIPT_DIR'] = os.path.dirname(environ['SCRIPT_NAME'])
    response.write("</ul>\n")
    response.write("<p>You can access a <a href='" + os.path.dirname(request.META['SCRIPT_NAME']) + "/static/index.html'>file</a> in my <em>static</em> directory.")
    
    parse_rule("ans1 and ans3 : ans22 red9", request.user)

    return response


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


# definition for a set of questions
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
#important      # If any other answers need to be answered implicitly do it here
                # Check rule base
                # Save answer in the same way but with the implicit column set to 1
            else:
                answered.answer = selected_answer
                answered.save()
#important      # Check the rule base and implictly answered questions
                # Implicit answers may need to be removed
        elif q not in request.session:
            # Save answer in session dict
 	        request.session[q] = selected_answer
#important  Check rule base, answers may implicity answer other questions
            # Maybe store q+'implicit' as the key and 0 or 1 as the value
        else:
            # Delete the old answer before adding the new one
            del request.session[q]
            request.session[q] = selected_answer
#important  # Check the rule base and implictly answered questions
            # Implicit answers may need to be removed
        
        if qpath != None:
            #nextq = qpath.follow_question
            nextq = get_next_question_or_none(request.user)

        if qpath == None:
            return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('questions/detail.html', {'question': nextq}, context_instance=RequestContext(request))

# Renders results to questions
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
#important          # Other answers may need be changed depending on the rules
                return HttpResponseRedirect(reverse("profile"))
            else:   
                if q in request.session:
                    # Delete the old answer before adding the new one
                    del request.session[q]
                    request.session[q] = selected_answer
#important          # Other answers may need be changed depending on the rules
    
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

# Save current user state. Render same state on login
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


# View registered user count
def record_view(request):
    count = User.objects.count()
    return render_to_response('questions/record_view.html', {'count': count}, context_instance=RequestContext(request))



# adrian, what does this do?
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



# links to help templates
def help(request):
    if request.user.is_staff:
        return render_to_response('questions/help_staff.html', {}, context_instance=RequestContext(request))
    else:
        return render_to_response('questions/help_user.html', {}, context_instance=RequestContext(request))
