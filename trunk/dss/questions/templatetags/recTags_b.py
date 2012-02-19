from dss.recommendations.models import Recommendation,RecAnswerLink
from django.template import Library,Node

register = Library()

def build_tag_list(parser,token):
    """
    {% get_tag_list %}
    """
    return TagMenuObject()

class TagMenuObject(Node):
    def render(self,context):
        output = ['']

    for i in Recommendation.objects.all():
        number = i.post_set.count()
        if number >= 1:
            output.append(i)
    context["rec_tags"] = output
    return ""

register.tag("get_tag_list",build_tag_list)
