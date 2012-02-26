import datetime
from django.db import models
from django.contrib.auth.models import User
from dss.auth.models import Profile
from django.forms import ModelForm

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class Answer(models.Model):
    # The following is if you want to limit the answer choices to Yes and No
    #ANSWER_CHOICES = (
    #    ('Yes', 'Yes'),
    #    ('No', 'No'),
    #)
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=200)#, choices=ANSWER_CHOICES)    
    def __unicode__(self):
        return self.question.question+" "+self.answer


class AnsweredQuestion(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
    	return self.answer.answer
    #Each user has a number of questions to answer
    class Meta:
        unique_together = ('user', 'question',)

    
class Recommendation(models.Model):
    recommendation = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.recommendation
    #A user may have one or more recommendations
    class Meta:
        order_with_respect_to = 'user'
    #Making recommendations based on userprofiles
    class Meta:
        unique_together = ('user', 'recommendation',)



class QuestionPath(models.Model):
    profile = models.ForeignKey(Profile)
    current_question = models.ForeignKey(Question, related_name='current_question')
    follow_question = models.ForeignKey(Question, related_name='follow_question')
	
    def __unicode__(self):
	    return self.profile.name

#Form classes for a future build. 
class QuestionForm(ModelForm):
    class Meta:
        model = Question

class AnswerForm(ModelForm):
    class Meta:
        model = Answer

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
