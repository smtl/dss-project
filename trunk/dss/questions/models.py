import datetime
from django.db import models
from django.contrib.auth.models import User
from dss.auth.models import Profile

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

    class Meta:
        unique_together = ('user', 'question',)

    
class Recommendation(models.Model):
    recommendation = models.TextField()
    def __unicode__(self):
        return self.recommendation

class QuestionPath(models.Model):
    profile = models.ForeignKey(Profile)
    current_question = models.ForeignKey(Question, related_name='current_question')
    follow_question = models.ForeignKey(Question, related_name='follow_question')
	
    def __unicode__(self):
	    return self.profile.name
