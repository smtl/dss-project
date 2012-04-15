from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from auth.models import Profile, UserProfile
from django.template import RequestContext
from questions.models import AnsweredQuestion, Question
from django.core.urlresolvers import reverse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            up = UserProfile()
            up.user_id = new_user.id
            up.profile_id = 1
            up.save()
            return HttpResponseRedirect("{% url login %}")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })


def profile(request):
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        profile = user_profile.profile
        answered = AnsweredQuestion.objects.filter(user=request.user, redundancy=0)
        return render_to_response('auth/profile.html', {'answered_questions': answered, 'profile': profile}, context_instance=RequestContext(request))
    else:
        profile = Profile.objects.get(name="Default")
        answered = []
        for q in Question.objects.all():
            if q in request.session:
                if "r"+q.question not in request.session:
                    answered.append(request.session[q])
        return render_to_response('auth/profile.html', {'answered_questions': answered, 'profile': profile}, context_instance=RequestContext(request))


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def change_profile(request):
    if request.method == 'POST':
        # Check to see if the user already has a profile. If they do we want to edit rather than creating a new one.
        current_profile = get_or_none(UserProfile, user=request.user)
        if current_profile != None:
            current_profile.profile_id = request.POST['p']
            current_profile.save()
            old_answers = AnsweredQuestion.objects.filter(user=request.user)
            old_answers.delete()
        else:
            p = UserProfile()
            p.profile_id = request.POST['p']
            p.user = request.user
            p.save()   
        return HttpResponseRedirect(reverse('profile'))
    else:
        pc = Profile.objects.all()
        return render_to_response("auth/change_profile.html", {
        'profilechoice': pc
    }, context_instance=RequestContext(request))
    

