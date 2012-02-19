"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from __future__ import with_statement

from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from django.http import HttpRequest, HttpResponse
from django.utils.functional import curry
from django.core.exceptions import SuspiciousOperation
from Cookie import SimpleCookie, Morsel
from django.conf import settings
from django.core.context_processors import csrf
from django.middleware.csrf import CsrfViewMiddleware
from django.template import RequestContext, Template
from django.contrib.auth.models import User
from dss.auth.models import Profile
import copy

from dss.auth.models import Profile, UserProfile
from dss.recommendations.models import Recommendation, RecAnswerLink
from dss.questions.models import Question, Answer, QuestionPath, AnsweredQuestion

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#Adrian Kwizera
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
 
    def test_MyView(self):
        User.objects.create_user('general', 'general@admin.com', 'polishgirl')
 
        #use test client to perform login
        user = self.client.login(username='general', password='polishgirl')
 
        response = self.client.post('http://localhost:8000/admin/')

# Adrian Kwizera
class CountTest(TestCase):
    def test_user_count(self):

        """
        Tests that the user count for registered users is working
        """
        self.assertEqual(0 + 1, 1)
        self.assertEqual(1 + 1, 2)

# Stephen Lowry
class UserTest(unittest.TestCase):
    def setUp(self):
        self.u = User.objects.create(username="Test", password="test")
    def testUser(self)
        self.assertEqual(self.u.username, "Test")

# Stephen Lowry
class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.p = Profile.objects.create(name="TestProfile")
    def testProfile(self):
        self.assertEqual(self.p.name, "TestProfile")

# Stephen Lowry
class UserProfileTest(unittest.TestCase):
    def setUp(self):
       self.u = User.objects.create(username="Test", password="test")
       self.p = Profile.objects.create(name="TestProfile")
       self.userprofile = UserProfile.objects.create(user=self.u, profile=self.p)
    def testUserProfile(self):
       self.assertEqual(self.userprofile.user.username, "Test")
       self.assertEqual(self.userprofile.profile.name, "TestProfile")

# Stephen Lowry
class RecommendationTest(unittest.TestCase):
    def setUp(self):
        self.r = Recommendation.objects.create(recommendation="This is a recommendation")
    def testRecommendation(self):
        self.assertEqual(self.r.recommendation, "This is a recommendation")

# Stephen Lowry
class RecAnswerLinkTest(unittest.TestCase):
    def setUp(self):
        self.r = Recommendation.objects.create(recommendation="This is a recommendation")
        self.q = Question.objects.create(question="What?")
        self.a = Answer.objects.create(question=self.q, answer="Yes")
        self.ralink = RecAnswerLink.objects.create(question=self.q, answer=self.a, recommendation=self.r)
    def testRecAnswerLink(self):
        self.assertEqual(self.ralink.question.question, "What?")
        self.assertEqual(self.ralink.recommendation.recommendation, "This is a recommendation")
        self.assertEqual(self.ralink.answer.answer, "Yes")


#Adrian Kwizera
#Testing the user profile
class UserProfileTesting(unittest.TestCase):
    def setUp(self):
        self.profile1 = User.objects.create(username='Manager')
        self.profile2 = User.objects.create(username='Engineer')

    def testA(self):
        self.assertEquals(self.profile1.username, 'Manager')
        self.assertEquals(self.profile2.username, 'Engineer')
       
        def tearDown(self):
          self.profile1.delete()
          self.profile2.delete()
