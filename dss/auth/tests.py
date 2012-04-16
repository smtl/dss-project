"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from auth.models import Profile
from auth.models import Profile, UserProfile
from recommendations.models import Recommendation, RecAnswerLink
from questions.models import Question, Answer, QuestionPath
from questions.models import AnsweredQuestion
from django.test.client import Client
from auth.views import get_or_none

# Stephen Lowry

class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.u = User.objects.create_user('charlie', 'charlie@charlie.com', 'charlie')
        self.p = Profile.objects.create(name="Default")
        self.up = UserProfile.objects.create(user=self.u, profile=self.p)

    def test_model(self):
        self.assertEqual(self.p.name, "Default")

    def test_profile(self):
        c = Client()
        response = c.get('/profile/')
        self.assertEqual(response.status_code, 200)

        user = c.login(username='charlie', password='charlie')
        self.assertEqual(user, True)

        response = c.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_get_or_none(self):
        self.pr = get_or_none(Profile, name="Default")
        self.assertEqual(self.pr.name, "Default")
        self.pr2 = get_or_none(Profile, name="Random")
        self.assertEqual(self.pr2, None)

    def test_change_profile(self):
        c = Client()

        user = c.login(username='charlie', password='charlie')
        self.assertEqual(user, True)        
        
        response = c.get('/profile/')
        self.assertEqual(response.status_code, 200)

        response = c.post('/changeprofile/', {'p': '1'})
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.u.delete()
        self.p.delete()
        self.up.delete()


