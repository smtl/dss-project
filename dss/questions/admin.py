from dss.questions.models import Question, Answer
from django.contrib import admin

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ('Question', {'fields': ['question']}),
    ]
    inlines = [AnswerInline]
    #list_display = ('question')
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
