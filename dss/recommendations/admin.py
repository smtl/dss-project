from recommendations.models import Recommendation, RecommendationProfile, UploadedFile, RecAnswerLink
from questions.models import Question, Answer
from django.contrib import admin
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

class RecommendationProfileInline(admin.TabularInline):
    model = RecommendationProfile
    extra = 0
    fieldsets = [
        (RecommendationProfile, {
            'fields': ('recommendation', 'profile',)
        })
    ]

class RecommendationAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Recommendation', {'fields': ['name','recommendation']}),
    ]
    inlines = [RecommendationProfileInline] 
    search_fields = ['recommendation']


class UploadedFileAdmin(admin.ModelAdmin):
    fieldsets = [
       ("UploadedFile", {"fields": ["files"]}),
    ]
    search_fields = ["files"]

class RecAnswerLinkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Recommendation Answer Link', {'fields': ['recommendation','answer']}),
    ]
    search_fields = ['recommendation', 'answer']


class MultipleFactsInline(admin.TabularInline):
    model = RecommendationProfile
    extra = 0
    fieldsets = [
        (RecommendationProfile, {
            'fields': ('recommendation', 'profile',)
        })
    ]


class MultipleFilesAdmin(admin.ModelAdmin):
    fieldsets = [
       ("Multiple Fact", {"fields": ["recommendation"]}),
    ]
    search_fields = ["recommendation"]

class RuleAdmin(admin.ModelAdmin):
    def rules(self, request):
        return admin_rules(request, self)

    def get_urls(self):
        urls = super(RuleAdmin, self).get_urls()
        my_urls = patterns('', (r'^rules/$', self.rules))
        return my_urls + urls

@staff_member_required
def admin_rules(request, model_admin):
    opts = model_admin.model._meta
    admin_site = model_admin.admin_site
    has_perm = request.user.has_perm(opts.app_label+'.'+opts.get_change_permission())
    
    # To show rules already in system
    rule_list = []
    for ru in Rule.objects.all():
        rule_list.append(ru)

    # To display answers to choose from
    answer_list = []
    for a in Answer.objects.all():
        answer_list.append(a)
    
    # To display recommendations to choose from
    rec_list = []
    for r in Recommendation.objects.all():
        rec_list.append(r)

    # To display questions to choose from (to make redundant)
    question_list = []
    for q in Question.objects.all():
        question_list.append(q)

    # To choose bool operator to choose from
    bool_list = ["and", "or"]
    
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
    template = 'admin/recommendations/recommendation/rules.html'
    return render_to_response(template, context, context_instance=RequestContext(request))

#admin.site.register(Rule, RuleAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)
#admin.site.register(RecAnswerLink, RecAnswerLinkAdmin)
