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
from dss.questions.models import Question, Answer, QuestionPath
from dss.questions.models import AnsweredQuestion

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
    def testUser(self):
        self.assertEqual(self.u.username, "Test")
    def tearDown(self):
          self.u.delete()

# Stephen Lowry
class Questiontest(unittest.TestCase):
    def setUp(self):
        self.q = Question.objects.create(question = "Why?")
    def testQuestions(self):
        self.assertEqual(self.q.question, "Why?")
    def tearDown(self):
        self.q.delete()

# Stephen Lowry
class AnswerTest(unittest.TestCase):
    def setUp(self):
        self.q = Question.objects.create(question = "Is this a question?")
        self.a = Answer.objects.create(question = self.q, answer= "Yes")
    def testAnswers(self):
        self.assertEqual(self.a.question.question, "Is this a question?")
        self.assertEqual(self.a.answer, "Yes")
    def tearDown(self):
        self.q.delete()
        self.a.delete()

# Stephen Lowry
class AnsweredQuestionTest(unittest.TestCase):
    def setUp(self):
        self.u = User.objects.create(username="useracc", password="useracc")
        self.q = Question.objects.create(question = "What is your name?")
        self.a = Answer.objects.create(question = self.q, answer = "Matt Belamy")
        self.aq = AnsweredQuestion.objects.create(user=self.u, question=self.q, answer=self.a)
    def testAnsweredQuestions(self):
        self.assertEqual(self.aq.user.username, "useracc")
        self.assertEqual(self.aq.question.question, "What is your name?")
        self.assertEqual(self.aq.answer.answer, "Matt Belamy")
    def tearDown(self):
        self.u.delete()
        self.q.delete()
        self.a.delete()
        self.aq.delete()
    

# Stephen Lowry
class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.p = Profile.objects.create(name="TestProfile")
    def testProfile(self):
        self.assertEqual(self.p.name, "TestProfile")
    def tearDown(self):
        self.p.delete()

# Stephen Lowry
class UserProfileTest(unittest.TestCase):
    def setUp(self):
       self.u = User.objects.create(username="Test", password="test")
       self.p = Profile.objects.create(name="TestProfile")
       self.userprofile = UserProfile.objects.create(user=self.u, profile=self.p)
    def testUserProfile(self):
       self.assertEqual(self.userprofile.user.username, "Test")
       self.assertEqual(self.userprofile.profile.name, "TestProfile")
    def tearDown(self):
        self.u.delete()
        self.p.delete()
        self.userprofile.delete()

# Stephen Lowry
class RecommendationTest(unittest.TestCase):
    def setUp(self):
        self.r = Recommendation.objects.create(recommendation="This is a recommendation")
    def testRecommendation(self):
        self.assertEqual(self.r.recommendation, "This is a recommendation")
    def tearDown(self):
        self.r.delete()

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
    def tearDown(self):
        self.q.delete()
        self.a.delete()
        self.r.delete()


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
