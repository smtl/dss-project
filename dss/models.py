from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=200)
    def __unicode__(self):
        return self.answer

"""
Empty file, mark package as valid django application
"""
