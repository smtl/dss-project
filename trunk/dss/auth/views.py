from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from dss.auth.models import Profile, UserProfile
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })

@login_required
def profile(request):
    try:
        profile = request.user.get_profile()
    except:
        return HttpResponseRedirect("/changeprofile/")

    user_profile = request.user.get_profile()
    profile = user_profile.profile
    return render_to_response("auth/profile.html", {
        'profile': profile,
    }, context_instance=RequestContext(request))

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
        else:
            p = UserProfile()
            p.profile_id = request.POST['p']
            p.user = request.user
            p.save()
        return HttpResponseRedirect('/profile/')
    else:
        pc = Profile.objects.all()
        return render_to_response("auth/change_profile.html", {
        'profilechoice': pc
    }, context_instance=RequestContext(request))
    

