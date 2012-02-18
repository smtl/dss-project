from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    profile = models.ForeignKey(Profile)
    def __unicode__(self):
        return self.profile

