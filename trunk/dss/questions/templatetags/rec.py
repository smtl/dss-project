from dss.recommendations.models import Recommendation, RecAnswerLink, RecommendationProfile
from dss.auth.models import Profile
from dss.questions.models import AnsweredQuestion, Question
from django.template import Library, Node
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import os
import glob

register = Library()


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def build_rec_list(parser,token):
    """
    {% get_rec_list %}
    """
    return RecObj()
   

class RecObj(Node):
    def render(self,context):
        # New way of doing this
        # Go through all the recommendations and get the answer links. If all the answers are in the user's database, present the answer 
        # Get the page request so we know who the user is
        if 'request' in context:
            request = context['request']
        
        # If they are signed in we query the database
        if request.user.is_authenticated():
            rec_answers = []
            recos = []
            user_answers=[]
            qa = AnsweredQuestion.objects.filter(user=request.user)
            for ua in qa:
                user_answers.append(ua.answer)
            for r in Recommendation.objects.all():
                rec_answer_links = RecAnswerLink.objects.filter(recommendation = r)
                for a in rec_answer_links:
                    rec_answers.append(a.answer)
                if set(rec_answers).issubset(set(user_answers)):
                    recos.append(r)
                rec_answers = []

            recpro = RecommendationProfile.objects.filter(profile=request.user.get_profile().profile)
            for re in recpro:
                if re.recommendation in recos:
                    recos.remove(re.recommendation)
                    recos.insert(0,re.recommendation)  

            context['rec'] = recos

        # Guest stuff
        else:
            # Get all the answers a guest has given
            guest_answers = []
            recos = []
            rec_answers = []
            for q in Question.objects.all():
                if q in request.session:
                    guest_answers.append(request.session[q])
            for r in Recommendation.objects.all():
                rec_answer_links = RecAnswerLink.objects.filter(recommendation = r)
                for a in rec_answer_links:
                    rec_answers.append(a.answer)
                if set(rec_answers).issubset(set(guest_answers)):
                    recos.append(r)
                rec_answers = []

            p = Profile.objects.get(name="Default")
            recpro = RecommendationProfile.objects.filter(profile=p)
            for re in recpro:
                if re.recommendation in recos:
                     recos.remove(re.recommendation)
                     recos.insert(0,re.recommendation)  

            context['rec'] = recos
        return ""

register.tag("get_rec_list",build_rec_list)

@register.filter
@stringfilter
def media(value,arg):
    if "iframe" in value:
        return value
    elif "http" in value or "www." in value:
        return "<a href=\""+value+"\">link</a>"
    elif ".avi" in value or ".mpg" in value or ".mp4" in value:
        filename = value.split("/")[-1]
        os.system("mv "+value+" media/"+filename)
        return "<a href=\""+"media/"+filename+"\">local video link</a>"
    else:
        return value
register.filter("media",media)


def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)



