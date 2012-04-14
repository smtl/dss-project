from django.db import models

class Rule(models.Model):
    rule = models.CharField(max_length="110")

    def __unicode__(self):
        return self.rule
