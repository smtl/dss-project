from recommendations.models import Recommendation, RecAnswerLink, UploadedFile
from questions.models import Question, Answer, AnsweredQuestion
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
'''
def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
'''
'''
def show(request):
    # user is logged in user
    if request.user.is_authenticated():
        answers = AnsweredQuestion.objects.filter(user=request.user.id)
        for a in answers:
            recs = RecAnswerLink.objects.filter(answer=a)
        return render_to_response('recommendations/show.html', {'recs': recs})
    else:
        return render_to_response('questions/index.html', {})

def rules(request):
    return render_to_response('questions/index.html', {}, RequestContext(request, {}))
rules = staff_member_required
'''
