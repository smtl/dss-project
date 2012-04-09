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
    print "This is the bool_rule: "+bool_rule
    tokens = bool_rule.split(' ')
    result_tokens = result_part.split(' ')
    new_rule = bool_rule
    current_user = request.user
    # create the logic string
    for t in tokens:
        if 'ans' in t:
            current_answer = get_or_none(Answer, id=int(float(t[3:])))
            # Handle users and guests differently
            if request.user.is_authenticated():
                ans_bool_result = get_or_none(AnsweredQuestion, user=current_user, answer=current_answer)
            elif current_answer.question in request.session:
                ans_bool_result = "question found"
            else:
                ans_bool_result = None

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
        # Actions for the outcomes of a rule
        for t in result_tokens:
            # red denotes redundancy
            if "red" in t:
                print "outcome results in a question being made redundant"
                question = get_or_none(Question, id=int(float(t[3:])))
                # check if question has already been answered, if it has there is no point marking it redundant
                # actually this is a design decision - it can be changed if neccesary
                if current_user.is_authenticated():
                    answered = get_or_none(AnsweredQuestion, user=current_user, question=question)
                elif question in request.session:
                    answered = "question found"
                else:
                    answered = None

                if answered == None:
                    if current_user.is_authenticated():
                        aq = AnsweredQuestion()
                        aq.user = current_user
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
                if current_user.is_authenticated():
                    recommended = get_or_none(UserRecommendation, user=current_user, recommendation=rec)
                elif rec in request.session:
                    recommended = request.session[rec]
                else:
                    recommended = None

                if recommended == None:
                    if current_user.is_authenticated():
                        ur = UserRecommendation()
                        ur.user = current_user
                        ur.recommendation = rec
                        ur.save()
                    else:
                        request.session[rec] = rec
            # answer denotes to answer a question implictly
            elif "ans" in t:
                print "outcome results in marking a answer as implicitly answered"
                # check if question is already answered by user. If it is, there is no need to mark it implicit
                answer = get_or_none(Answer, id=int(float(t[3:])))
                if current_user.is_authenticated():
                    answered = get_or_none(AnsweredQuestion, user=current_user, question=answer.question)
                elif answer.question in request.session:
                    answered = "Not None"
                else:
                    answered = None

                if answered == None:
                    if current_user.is_authenticated():
                        aq = AnsweredQuestion()
                        aq.user = current_user
                        aq.question = answer.question
                        aq.answer = answer
                        aq.implicit = 1
                        aq.save()
                    else:
                        request.session["i"+answer.question.question] = answer
    else:
        print "false lol"

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
        
        # test parse stuff
        #parse_rule("ans1 and ans3 : rec13 red13 ans12", context)
        new_rec_list = []
        if request.user.is_authenticated():
            new_recs = UserRecommendation.objects.filter(user=request.user)
            for r in new_recs:
                new_rec_list.append(r)
        else:
            for r in Recommendation.objects.all():
                if r in request.session:
                    new_rec_list.append(r)
        
        #context['rec'] = new_rec_list
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
                if len(rec_answers) > 0 and set(rec_answers).issubset(set(user_answers)):
                    recos.append(r.recommendation)
                rec_answers = []

            recpro = RecommendationProfile.objects.filter(profile=request.user.get_profile().profile)
            for re in recpro:
                if re.recommendation in recos:
                    recos.remove(re.recommendation.recommendation)
                    recos.insert(0,re.recommendation.recommendation)  

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
                if len(rec_answers) > 0 and set(rec_answers).issubset(set(guest_answers)):
                    recos.append(r.recommendation)
                rec_answers = []

            p = Profile.objects.get(name="Default")
            recpro = RecommendationProfile.objects.filter(profile=p)
            for re in recpro:
                if re.recommendation in recos:
                     recos.remove(re.recommendation.recommendation)
                     recos.insert(0,re.recommendation.recommendation)  

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



