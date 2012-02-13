import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class Answer(models.Model):
    ANSWER_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=200, choices=ANSWER_CHOICES)
    def __unicode__(self):
        return self.question.question+" "+self.answer

class AnsweredQuestion(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    
class Recommendation(models.Model):
    recommendation = models.TextField()
    def __unicode__(self):
        return self.recommendation

class Guest(models.Model):
    
    """
    A temporary user.

    Fields:
    ``user`` - The temporary user.
    ``last_used`` - The last time we noted this user doing something.
    
    All users with a record in this model are temporary and should be
    deleted after GUEST_DELETE_TIME.
    
    """

    user = models.ForeignKey(User)
    last_used = models.DateTimeField(User)

    @classmethod
    def create_guest(self, user):
        guest = Guest(user=user, last_used=datetime.datetime.now())
        return guest
