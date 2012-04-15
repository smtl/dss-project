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
from rules.models import Rule

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def deleterule(request):
    if request.method == "POST":
        rule_string = request.POST['deleterule']
        id_string = rule_string.split(" ")[1]
        print id_string
        rule = get_or_none(Rule, pk=int(float(id_string[3:])))
        if rule != None:
            rule.delete()
        return HttpResponseRedirect(reverse("admin:rules_rule_changelist"))
    #return render_to_response('questions/results.html', {}, context_instance=RequestContext(request))

