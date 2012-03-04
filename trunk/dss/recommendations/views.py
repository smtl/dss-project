from dss.recommendations.models import Recommendation, RecAnswerLink, UploadedFile
from dss.questions.models import Question, Answer, AnsweredQuestion
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


"""def handle_uploaded_file(request):
    dest = open("/media/sample","w")
    dest.write("Hello there!")
    dest.close()
"""

"""def uploadFile(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/questions/1/")
        else:
            form = UploadFileForm()
        return render_to_response("/recommendations/",{"form":form}
"""
def show(request):
    # user is logged in user
    if request.user.is_authenticated():
        answers = AnsweredQuestion.objects.filter(user=request.user.id)
        for a in answers:
            recs = RecAnswerLink.objects.filter(answer=a)
        return render_to_response('recommendations/show.html', {'recs': recs})
    else:
        return render_to_response('questions/index.html', {})
