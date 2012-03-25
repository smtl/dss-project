from django.contrib.auth.models import User
from django.template import Library, Node

register = Library()

def build_count(parser,token):
    """
    {% get_count %}
    """
    return RecObj()
   

class RecObj(Node):
    def render(self,context):

        context['count'] = User.objects.count()
        return ""

register.tag("get_count",build_count)
