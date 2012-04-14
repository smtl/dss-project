from recommendations.models import Recommendation, RecommendationProfile, UploadedFile, RecAnswerLink
from rules.models import Rule
from questions.models import Question, Answer
from django.contrib import admin
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
import re

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

class RuleAdmin(admin.ModelAdmin):
    def rules(self, request):
        return admin_rules(request, self)

    def get_urls(self):
        urls = super(RuleAdmin, self).get_urls()
        my_urls = patterns('', (r'^rules/$', self.rules))
        return my_urls + urls

@staff_member_required
def admin_rules(request, model_admin=None):
    if request.method == 'POST':
        # get information that was submitted
        part1 = request.POST['part1']
        boolpart = request.POST['boolpart']
        part2 = request.POST['part2']

        # build up the boolean part of the rule
        boolstring = ""
        if part1:
            boolstring += "ans"+part1
            if boolpart != "None":
                if part2:
                    boolstring += " "+boolpart+" ans"+part2
        print boolstring

        # results part
        rec_result = request.POST['result1']
        ans_result = request.POST['result2']
        red_result = request.POST['result3']
        resultstring = ""
        
        if rec_result:
            rec_result="rec"+rec_result
        if ans_result:
            ans_result="ans"+ans_result
        if red_result:
            red_result="red"+red_result

        temp_result_list = [rec_result, ans_result, red_result]
        for r in temp_result_list:
                resultstring = resultstring+r+" "
        
        if len(boolstring) > 1 and (len(resultstring) > 1):
            rule = Rule()
            rule.rule = boolstring+" : "+resultstring
            rule.save()

        #return render_to_response('admin/rules/rule/rules.html', {}, context_instance=RequestContext(request))

    opts = model_admin.model._meta
    admin_site = model_admin.admin_site
    has_perm = request.user.has_perm(opts.app_label+'.'+opts.get_change_permission())
    
    # To show rules already in system
    rule_list = []
    for ru in Rule.objects.all():
        rule = ""
        result_str = ""
        bool_rule = re.compile(":").split(ru.rule)[0]
        result_part = re.compile(":").split(ru.rule)[1]
        print result_part
        tokens = bool_rule.split(' ')
        result_tokens = result_part.split(" ")
        for t in tokens:
            if "ans" in t:
                temp_ans = get_or_none(Answer, pk=(int(float(t[3:]))))
                if temp_ans != None:
                    rule += str(temp_ans)
            if t == "and" or t == "or":
                rule += " <strong>"+t+"</strong> "
        
        result_str += "<br /><strong>triggers the following:</strong><ul> "
        for rt in result_tokens:
            if "rec" in rt:
                temp_rec = get_or_none(Recommendation, pk=(int(float(rt[3:]))))
                if temp_rec != None:
                    result_str += "<li>A recommendation: "+str(temp_rec)+"</li>"
            
            if "ans" in rt:
                temp_ans_result = get_or_none(Answer, pk=(int(float(rt[3:]))))
                if temp_ans_result != None:
                    result_str += "<li>A question being implicitly answered: "+str(temp_ans)+"</li>"
            
            if "red" in rt:
                temp_red = get_or_none(Question, pk=(int(float(rt[3:]))))
                if temp_red != None:
                    result_str += "<li>A question being made redundant: "+str(temp_red)+"</li>"


        rule_list.append(rule+result_str+"</ul>")
    
    # To display answers to choose from
    answer_list = []
    for a in Answer.objects.all():
        answer_list.append(a)
    answer_list.append("None")
    
    # To display recommendations to choose from
    rec_list = []
    for r in Recommendation.objects.all():
        rec_list.append(r)
    rec_list.append("None")
    
    # To display questions to choose from (to make redundant)
    question_list = []
    for q in Question.objects.all():
        question_list.append(q)
    question_list.append("None")

    # To choose bool operator to choose from
    bool_list = ["and", "or", "None"]
    
    context = {'admin_site': admin_site.name,
                'title': "Create Custom Rules",
                'opts': opts,
                'root_path': '/%s' % admin_site.root_path,
                'app_label': opts.app_label,
                'has_change_permission': has_perm,
                'question_list': question_list,
                'rec_list': rec_list,
                'rule_list': rule_list,
                'answer_list': answer_list,
                'bool_list': bool_list
                }
    template = 'admin/rules/rule/rules.html'
    return render_to_response(template, context, context_instance=RequestContext(request))

admin.site.register(Rule, RuleAdmin)
