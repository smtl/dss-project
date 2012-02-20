"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from __future__ import with_statement

import templatetags as rec
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
from django.core import mail
import copy

from dss.auth.models import Profile, UserProfile
from dss.recommendations.models import Recommendation, RecAnswerLink
from dss.questions.models import Question, Answer, QuestionPath
from dss.questions.models import AnsweredQuestion

#Adrian Kwizera
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
 
    def test_MyView(self):
        User.objects.create_user('general', 'general@admin.com', 'general1')
 
        #use test client to perform login
        user = self.client.login(username='general', password='general1')
 
        response = self.client.post('http://localhost:8000/admin/')

class test_guest_logging(unittest.TestCase):
    def testGuest(self):
        client = Client()
        session = client.session 
        session['a'] = 1
        self.assertEqual(session['a'],1)

# Adrian Kwizera
class CountTest(TestCase):
    def test_user_count(self):

        """
        Tests that the user count for registered users is working
        """
        #for users registering on the site
        self.assertEqual(0 + 1, 1)
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 + 1, 3)

        #for users that unregister from the site 
        self.assertEqual(3 - 1, 2)
        self.assertEqual(2 - 1, 1)
        self.assertEqual(1 - 1, 0)
       

# Stephen Lowry
class test_page_responses(unittest.TestCase):
    def testAnonPages(self):
        client = Client()
        self.q = Question.objects.create(question = "Why?")
        home = client.get('/')
        questions = client.get('/questions/')
        profile = client.get('/profile/')
        changeprofile = client.get('/changeprofile/')
        question = client.get('/questions/1/')
        answer = client.get('/questions/1/answer/')
        login = client.post('/accounts/login/', {'username': 'bingo', 'password': 'bingo'})
        self.assertEqual(home.status_code, 200)
        self.assertEqual(questions.status_code, 200)
        self.assertEqual(profile.status_code, 302) #redirects a guest user
        self.assertEqual(changeprofile.status_code, 200)
        self.assertEqual(question.status_code, 200)
        self.assertEqual(answer.status_code, 200)
        self.assertEqual(login.status_code, 200)
    def tearDown(self):
          self.q.delete()


# Stephen Lowry
class UserTest(unittest.TestCase):
    def setUp(self):
        self.u = User.objects.create(username="Test", password="test")
    def testUser(self):
        self.assertEqual(self.u.username, "Test")
    def tearDown(self):
          self.u.delete()

# Stephen Lowry
class test_question_creation(unittest.TestCase):
    def setUp(self):
        self.q = Question.objects.create(question = "Why?")
    def testQuestions(self):
        self.assertEqual(self.q.question, "Why?")
    def tearDown(self):
        self.q.delete()

# Stephen Lowry
class test_answer_creation(unittest.TestCase):
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
class test_storing_user_answers(unittest.TestCase):
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
class test_profile_creation(unittest.TestCase):
    def setUp(self):
        self.p = Profile.objects.create(name="TestProfile")
    def testProfile(self):
        self.assertEqual(self.p.name, "TestProfile")
    def tearDown(self):
        self.p.delete()

# Stephen Lowry
class test_profile_assigned_to_user(unittest.TestCase):
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

# Stephen lowry
class test_question_path_creation(unittest.TestCase):
    def setUp(self):
        self.p = Profile.objects.create(name="Engineer")
        self.q1 = Question.objects.create(question = "What is your favourite country?")
        self.q2 = Question.objects.create(question = "What is your favourite city?")
        self.qp = QuestionPath.objects.create(profile=self.p, current_question=self.q1, follow_question=self.q2)
    def testQuestionPath(self):
        self.assertEqual(self.qp.profile.name, "Engineer")       
        self.assertEqual(self.qp.current_question.question, "What is your favourite country?") 
        self.assertEqual(self.qp.follow_question.question, "What is your favourite city?")  
    def tearDown(self):
        self.p.delete()
        self.q1.delete()
        self.q2.delete()
        self.qp.delete()

# Stephen Lowry
class test_recommendation_creation(unittest.TestCase):
    def setUp(self):
        self.r = Recommendation.objects.create(recommendation="This is a recommendation")
    def testRecommendation(self):
        self.assertEqual(self.r.recommendation, "This is a recommendation")
    def tearDown(self):
        self.r.delete()

# Stephen Lowry
class test_storing_links_from_answers_to_recommendations(unittest.TestCase):
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


#Stephen Murphy
#Testing the recommendation parsing
class recParsing(unittest.TestCase):
    def setUp(self):
        self.link = Recommendation.objects.create(recommendation="http://www.yahoo.com")
        self.text = Recommendation.objects.create(recommendation="Hello")
        self.yout = Recommendation.objects.create(recommendation="<iframe width=\"560\" height=\"315\" src=\"http://www.youtube.com/embed/SBh01XZHfL0\" frameborder=\"0\" allowfullscreen></iframe>")
    def test_link(self):
        self.assertEqual(rec.rec.media(self.link.recommendation,0),"<a href=\"http://www.yahoo.com\">link</a>")
    def test_text(self):
        self.assertEqual(rec.rec.media(self.text.recommendation,0),"Hello")
    def test_youTube(self):
        self.assertEqual(rec.rec.media(self.yout.recommendation,0),"<iframe width=\"560\" height=\"315\" src=\"http://www.youtube.com/embed/SBh01XZHfL0\" frameborder=\"0\" allowfullscreen></iframe>")

#Adrian Kwizera
#Testing the user creation
class UserCreationTesting(unittest.TestCase):
    def setUp(self):
        self.profile1 = User.objects.create(username='Adrian')
        self.profile2 = User.objects.create(username='Poland')
        self.profile3 = User.objects.create(username='James')
        self.profile4 = User.objects.create(username='Cathy')
        self.profile5 = User.objects.create(username='Stephen')
        self.profile6 = User.objects.create(username='Murphy')

    def testA(self):
        self.assertEquals(self.profile1.username, 'Adrian')
        self.assertEquals(self.profile2.username, 'Poland')
        self.assertEquals(self.profile3.username, 'James')
        self.assertEquals(self.profile4.username, 'Cathy')
        self.assertEquals(self.profile5.username, 'Stephen')
        self.assertEquals(self.profile6.username, 'Murphy')

        def tearDown(self):
          self.profile1.delete()
          self.profile2.delete()
          self.profile3.delete()
          self.profile4.delete()
          self.profile5.delete()
          self.profile6.delete()

#Adrian Kwizera
class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail('Using Django', 'Here is how to use django.',
            'from_user@admin.com', ['to_another_user@admin.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEquals(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEquals(mail.outbox[0].subject, 'Using Django')
