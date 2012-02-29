from dss.recommendations.models import Recommendation, RecAnswerLink
from dss.questions.models import AnsweredQuestion
from django.template import Library, Node
from django.template.defaultfilters import stringfilter
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
        # Get the page request so we know who the user is
        if 'request' in context:
            request = context['request']
        # If they are signed in we query the database
        if request.user.is_authenticated():
            
            # Get all of the user's answers
            user_answers = AnsweredQuestion.objects.filter(user=request.user)
            full_list_of_rec_links = []
            rec_link_list = []

            # Go through the users answers and find the related recAnswerLink
            # This results in querysets for each answer
            for a in user_answers:
                rec_link_list.append(RecAnswerLink.objects.filter(answer=a.answer))
            
            # Go through list of querysets and get the full list of recAnswerLinks
            for rec_link in rec_link_list:
                for r in rec_link:
                    full_list_of_rec_links.append(r)
            
            recos = []
            # Get each specific recommendation
            for rec in full_list_of_rec_links:
                if rec != None:
                    recos.append(get_or_none(Recommendation, recommendation=rec.recommendation))
            context['rec'] = recos
        #else:
            #context['rec'] = Recommendation.objects.all()
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
