from recommendations.models import Recommendation, RecAnswerLink, RecommendationProfile
from auth.models import Profile
from questions.models import AnsweredQuestion, Question
from django.template import Library, Node
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import os
import glob
import re
from questions.models import Question, Answer, AnsweredQuestion
from recommendations.models import Recommendation, UserRecommendation

register = Library()

def parse_rule(rule, context):
    if 'request' in context:
        request = context['request']
    # rule is a string
    # "if 2 or 3 and 5 then r7"
    bool_rule = re.compile(":").split(rule)[0]
    result_part = re.compile(":").split(rule)[1]
    tokens = bool_rule.split(' ')
    result_tokens = result_part.split(' ')
    new_rule = bool_rule
    guest_answers = [] 
    # create the logic string
    for t in tokens:
        if 'ans' in t:
            ans_bool_result = None
            current_answer = get_or_none(Answer, id=int(float(t[3:])))
            print "Answer we are looking for: "+str(current_answer)
            # Handle users and guests differently
            if request.user.is_authenticated():
                print "answer found in useranswers"
                ans_bool_result = get_or_none(AnsweredQuestion, user=request.user, answer=current_answer)
            else:
                for q in Question.objects.all():
                    if q in request.session:
                        guest_answers.append(request.session[q])
                if current_answer in guest_answers:
                    print "answer found in guest answers"
                    print current_answer
                    ans_bool_result = "question found"
            
            if ans_bool_result == None:
                ans_bool = False
            else:
                ans_bool = True
            # create the new rule which is to be executed
            new_rule = new_rule.replace(t, str(ans_bool))
    
    # Build and execute the rule putting the result in the "result" variable
    result_string = "result = "+new_rule
    exec(result_string)
    if result == True:
        return result_tokens
    else:
        return None

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
        new_rec_list = []

        # test parse stuff
        result_tokens = parse_rule("ans1 and ans3 : rec1", context)
        
        if result_tokens != None:
            for t in result_tokens:
                # red denotes redundancy
                if "red" in t:
                    print "outcome results in a question being made redundant"
                    question = get_or_none(Question, id=int(float(t[3:])))
                    # check if question has already been answered, if it has there is no point marking it redundant
                    # actually this is a design decision - it can be changed if neccesary
                    if request.user.is_authenticated():
                        answered = get_or_none(AnsweredQuestion, user=request.user, question=question)
                    elif question in request.session:
                        answered = "question found"
                    else:
                        answered = None

                    if answered == None:
                        if request.user.is_authenticated():
                            aq = AnsweredQuestion()
                            aq.user = request.user
                            aq.question = question
                            aq.answer_id = 0
                            aq.redundancy = 1
                            aq.save()
                        else:
                            # redundancy marked by r at the start of the question
                            request.session["r"+question.question] = 0
                # rec denotes recommendation
                elif "rec" in t:
                    print "outcome results in a recommendation being recommended"
                    rec = get_or_none(Recommendation, id=int(float(t[3:])))
                    # check if recommendation is already recommended for user or guest
                    if rec != None:
                        new_rec_list.append(rec.recommendation)
                
                elif "ans" in t:
                    print "outcome results in marking a answer as implicitly answered"
                    # check if question is already answered by user. If it is, there is no need to mark it implicit
                    answer = get_or_none(Answer, id=int(float(t[3:])))
                    if request.user.is_authenticated():
                        answered = get_or_none(AnsweredQuestion, user=request.user, question=answer.question)
                    elif answer.question in request.session:
                        answered = "Not None"
                    else:
                        answered = None

                    if answered == None:
                        if request.user.is_authenticated():
                            aq = AnsweredQuestion()
                            aq.user = request.user
                            aq.question = answer.question
                            aq.answer = answer
                            aq.implicit = 1
                            aq.save()
                        else:
                            request.session["i"+answer.question.question] = answer
        # pass the list of recommendations back to be shown to user
        context['rec'] = new_rec_list
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



