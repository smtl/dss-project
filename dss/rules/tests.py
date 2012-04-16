"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from auth.models import Profile
from auth.models import Profile, UserProfile
from recommendations.models import Recommendation, RecAnswerLink
from questions.models import Question, Answer, QuestionPath
from questions.models import AnsweredQuestion
from rules.models import Rule
from rules.views import get_or_none

class RuleTest(unittest.TestCase):
    def setUp(self):
        self.r = Rule.objects.create(rule="ans2 : rec1")
        self.u = User.objects.create_user('harry', 'testfile@gmail.com', 'harry')
    
    def testModel(self):
        self.assertEquals(self.r.rule, "ans2 : rec1")

    def test_get_or_none(self):
        self.rr = get_or_none(Rule, rule="ans2 : rec1")
        self.assertNotEqual(self.rr.rule, None)

    def test_deleterule(self):
        c = Client()

        user = c.login(username='harry', password='harry')
        self.assertEqual(user, True)
        
        response = c.post('/admin/rules/rule/rules/deleterule/', {'deleterule':'rule id:1 Do you have employees abroad? Yes'})
        self.rr2 = get_or_none(Rule, pk=1)
        self.assertEqual(self.rr2, None)

        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.u.delete()
        self.r.delete()
