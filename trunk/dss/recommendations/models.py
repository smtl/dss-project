from django.db import models
from dss.questions.models import Answer, Question

# Create your models here.

class Recommendation(models.Model):
    recommendation = models.TextField()
    def __unicode__(self):
        return self.recommendation

class RecAnswerLink(models.Model):
    question = models.ForeignKey(Question)
    recommendation = models.ForeignKey(Recommendation)
    answer = models.ForeignKey(Answer)
    def __unicode__(self):
        return "Recommendation <-> Answer Link"
