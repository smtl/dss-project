from dss.questions.models import Question, Answer
from dss.recommendations.models import RecAnswerLink
from django.contrib import admin
from django import forms

#class OrderForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(OrderForm, self).__init__(*args, **kwargs)
#        self.fields['answer'].queryset = Answer.objects.filter(
#            recanswerlink=self.instance.id)

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

class RecAnswerLinkInline(admin.TabularInline):
#    form = OrderForm
    model = RecAnswerLink
    extra = 0
    fieldsets = [
        (Answer, {
            'fields': ('recommendation', 'answer',)
        })
    ]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Question', {'fields': ['question']}),
    ]
    inlines = [AnswerInline, RecAnswerLinkInline]
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
