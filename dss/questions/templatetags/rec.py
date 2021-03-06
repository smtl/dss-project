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
from rules.models import Rule

globalList = []

register = Library()

def parse_rule(rule, context):
    global globalList
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
    i=0
    for t in tokens:
        if 'ans' in t:
            ans_bool_result = None
            current_answer = get_or_none(Answer, id=int(float(t[3:])))
            # Handle users and guests differently
            if request.user.is_authenticated():
                ans_bool_result = get_or_none(AnsweredQuestion, user=request.user, answer=current_answer)
		if ans_bool_result != None:
			temp = "\n"+str(ans_bool_result.question)+" "+str(ans_bool_result)
	        tokens.remove(t)
            else:
                for q in Question.objects.all():
                    if q in request.session:
                        guest_answers.append(request.session[q])
                if current_answer in guest_answers:
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
	global globalList
        # New way of doing this
        # Go through all the recommendations and get the answer links. If all the answers are in the user's database, present the answer 
        # Get the page request so we know who the user is
        if 'request' in context:
            request = context['request']
        new_rec_list = []
	context["feedback"] = []

        # delete all redudant and implicitly answered questions here!!!!
        implicit_answers = AnsweredQuestion.objects.filter(implicit=1)
        implicit_answers.delete()
        redundant_questions = AnsweredQuestion.objects.filter(redundancy=1)
        redundant_questions.delete()
        #for a in Answer.objects.all():
        #    if ("i"+q.question) in request.session:
        #        print "removed implicit q for guest"
        #        del request.session["i"+a.question.question]
        #        if a.question in request.session:
        #            del request.session[a.question]
        for q in Question.objects.all():
        #    if ("r"+q.question) in request.session:
        #        print "removed redundant q for guest"
        #        del request.session["r"+q.question]
        #        if q in request.session:
        #            del request.session[q]
            if ("i"+q.question) in request.session:
                #print "i"+q.question
                del request.session["i"+q.question]
                if q in request.session:
                    del request.session[q]


        # test parse stuff
        #result_tokens = parse_rule("ans1 and ans3 : rec1", context)
        for ru in Rule.objects.all():
            result_tokens = parse_rule(ru.rule,context)
            if result_tokens != None:
                for t in result_tokens:
                    # red denotes redundancy
                    if "red" in t:
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
			#AUTHENTICATED USER
		        if request.user.is_authenticated():
                            rec = get_or_none(Recommendation, id=int(float(t[3:])))
                            # check if recommendation is already recommended for user or guest
                            if rec != None:
			        rul = (ru.rule).split(" : ")[0]
			        rul = rul.split(" ")
			        if len(rul) > 2:
			            if rul[1] == "or":
				        a = get_or_none(Answer, id=int(float(rul[0][3:])))
				        b = get_or_none(Answer, id=int(float(rul[2][3:])))
				        aa = get_or_none(AnsweredQuestion, user=request.user, answer=a)
				        bb = get_or_none(AnsweredQuestion, user=request.user, answer=b)
				        if aa is None:
				            globalList.append(str(bb.question.question)+" "+str(bb))
				        elif bb is None:
					    globalList.append(str(aa.question.question)+" "+str(aa))
				        elif aa is not None and bb is not None:
					    globalList.append(str(aa.question.question)+" "+str(aa))
					    globalList.append("or")
					    globalList.append(str(bb.question.question)+" "+str(bb))
				    elif rul[1] == "and":
				        a = get_or_none(Answer, id=int(float(rul[0][3:])))
				        b = get_or_none(Answer, id=int(float(rul[2][3:])))
				        aa = get_or_none(AnsweredQuestion, user=request.user, answer=a)
				        bb = get_or_none(AnsweredQuestion, user=request.user, answer=b)
				        globalList.append(str(aa.question.question)+" "+str(aa))
				        globalList.append("and")
				        globalList.append(str(bb.question.question)+" "+str(bb))
			        else:
				    a = get_or_none(Answer, id=int(float(rul[0][3:])))
			            aa = get_or_none(AnsweredQuestion, user=request.user, answer=a)
				    globalList.append(str(aa.question.question)+" "+str(aa))
			       # context["feedback"].extend(globalList)
			       # globalList = []
			   		 
			        recommend = "**this produces: **"+rec.name+"</b>"
                                context["feedback"].extend(globalList)
                                globalList = []
                                new_rec_list.append(rec.recommendation)
                                context["feedback"].append(recommend)
			#GUEST USER
                        else:
			    rec = get_or_none(Recommendation, id=int(float(t[3:])))
			    if rec not in request.session:
			        rul = (ru.rule).split(" : ")[0]
			        rul = rul.split(" ")
			        if len(rul) > 2:
				    a = get_or_none(Answer, id=int(float(rul[0][3:])))
				    b = get_or_none(Answer, id=int(float(rul[2][3:])))
				    if a.question in request.session and b.question in request.session:
			                if rul[1] == "or":
				            if (a != None) and (b != None):
				                a = get_or_none(Answer, id=int(float(rul[0][3:])))
				                b = get_or_none(Answer, id=int(float(rul[2][3:])))
					        globalList.append(str(request.session[a.question]))
					        globalList.append("or")
					        globalList.append(str(request.session[b.question]))
				            if (a == None) and (b != None):
				                a = get_or_none(Answer, id=int(float(rul[0][3:])))
				                b = get_or_none(Answer, id=int(float(rul[2][3:])))
				                globalList.append(str(request.session[b.question]))
				            elif (b == None) and (a != None):
				                a = get_or_none(Answer, id=int(float(rul[0][3:])))
				                b = get_or_none(Answer, id=int(float(rul[2][3:])))
					        globalList.append(str(request.session[a.question]))
				        elif rul[1] == "and":
				            a = get_or_none(Answer, id=int(float(rul[0][3:])))
				            b = get_or_none(Answer, id=int(float(rul[2][3:])))
					    if (a != None) and (b != None):
				                globalList.append(str(request.session[a.question]))
				                globalList.append("and")
				                globalList.append(str(request.session[b.question]))
			        else:
				    a = get_or_none(Answer, id=int(float(rul[0][3:])))
				    globalList.append(str(request.session[a.question]))
			       # context["feedback"].extend(globalList)
			       # globalList = []
			   		 
			        recommend = "**this produces: **"+rec.name+"</b>"
                                context["feedback"].extend(globalList)
                                globalList = []
                                new_rec_list.append(rec.recommendation)
                                context["feedback"].append(recommend)

				
                    elif "ans" in t:
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
                                request.session[answer.question] = answer
        # pass the list of recommendations back to be shown to user
        context['rec'] = new_rec_list
        return ""

register.tag("get_rec_list",build_rec_list)

'''
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
'''

'''
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)
'''
