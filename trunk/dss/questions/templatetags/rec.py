from dss.recommendations.models import Recommendation,RecAnswerLink
from django.template import Library,Node
from django.template.defaultfilters import stringfilter
import os
import glob

register = Library()

def build_rec_list(parser,token):
    """
    {% get_rec_list %}
    """
    return RecObj()


class RecObj(Node):
    def render(self,context):
        context['rec'] = Recommendation.objects.all()
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
