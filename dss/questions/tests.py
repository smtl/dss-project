"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib.auth import login, logout
import templatetags as rec
from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from django.middleware.csrf import CsrfViewMiddleware
from django.template import RequestContext, Template
from django.contrib.auth.models import User
from auth.models import Profile
from auth.models import Profile, UserProfile
from recommendations.models import Recommendation, RecAnswerLink
from questions.models import Question, Answer, QuestionPath
from questions.models import AnsweredQuestion
import tempfile
from questions.views import get_or_none, get_next_question_or_none, parse_rule
from questions.templatetags.rec import parse_rule

# Stephen Lowry
class QuestionTest(unittest.TestCase):
    def setUp(self):
        #self.u = User.objects.create(username='testfile', email='testfile@testfile.com', password='testfile')
        self.u = User.objects.create_user('testfile', 'testfile@gmail.com', 'testfile')
        self.q = Question.objects.create(question = "Why?")
        self.q2 = Question.objects.create(question = "How?")
        self.q.answer_set.create(answer="because")
        self.q.answer_set.create(answer="i don't know")
        self.q.answer_set.create(answer="another answer")
        self.a = Answer.objects.get(pk=1)
        self.a2 = Answer.objects.get(pk=2)
        self.p = Profile.objects.create(name="Default")
        self.up = UserProfile.objects.create(user=self.u, profile=self.p)
        self.qp = QuestionPath.objects.create(profile=self.p, current_question=self.q, follow_question=self.q2)
    
    def test_models(self):
        self.assertEqual(self.q.question, "Why?")
        self.assertEqual(self.q.answer_set.all().count(), 3)
        self.assertEqual(self.a.answer, "because") 

    def test_answer(self):
        c = Client()
        response = c.post('/questions/'+str(self.q.id)+'/answer/', {'answer':str(self.a.id), 'user_id':str(self.u.id)})
        self.assertEqual(response.status_code, 200)

        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)
        response = c.post('/questions/'+str(self.q.id)+'/answer/', {'answer':str(self.a.id), 'user_id':str(self.u.id)})
        self.assertEqual(response.status_code, 200)
        
        aq = AnsweredQuestion.objects.get(user=self.u, answer=self.a)
        self.assertEqual(aq.answer.answer, 'because')

    def test_details(self):
        c = Client()
        response = c.post('/questions/'+str(self.q.id)+'/')
        self.assertEqual(response.status_code, 200)

        user = c.login(username='testfile', password='testfile')
        response = c.post('/questions/'+str(self.q.id)+'/')

        self.assertEqual(response.status_code, 200)

    def test_index(self):
        c = Client()
        response = c.get('/index/')
        self.assertEqual(response.status_code, 200)

        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)

        response = c.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_results(self):
        c = Client()
        response = c.get('/questions/results/')
        self.assertEqual(response.status_code, 200)

        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)

        response = c.get('/questions/results/')
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        c = Client()
        response = c.post('/questions/'+str(self.q.id)+'/edit/')
        self.assertEqual(response.status_code, 200) 
        
        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)

        response = c.post('/questions/'+str(self.q.id)+'/answer/', {'answer':str(self.a.id), 'user_id':str(self.u.id)})
        self.assertEqual(response.status_code, 200)
        
        aq = AnsweredQuestion.objects.get(user=self.u, answer=self.a)
        self.assertEqual(aq.answer.answer, 'because')

        response = c.post('/questions/'+str(self.q.id)+'/edit/', {'answer':str(self.a2.id)})
        self.assertEqual(response.status_code, 302) 

        aq = AnsweredQuestion.objects.get(user=self.u, answer=self.a2)
        self.assertNotEqual(aq.answer.answer, "because")
        self.assertEqual(aq.answer.answer, "i don't know")

    def test_save_progress(self):
        c = Client()
        
        response = c.get('/save/')
        self.assertEqual(response.status_code, 200) 

        response = c.post('/save/', {'username':'bob', 'password1':'bob', 'password2':'bob'})
        user = c.login(username='bob', password='bob')
        self.assertEqual(user, True)
        response = c.get('/save/')
        self.assertEqual(response.status_code, 302)

    def test_help(self):
        c = Client()

        response = c.get('/help/')
        self.assertEqual(response.status_code, 200) 
        
        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)
        
        response = c.get('/help/')
        self.assertEqual(response.status_code, 200) 

    def test_get_or_none(self):
        self.qr = get_or_none(Question, question="Why?")
        self.assertEqual(self.qr.question, "Why?")
        self.qr2 = get_or_none(Question, question="Random")
        self.assertEqual(self.qr2, None)    
   
    def test_get_next_question_or_none(self):
        c = Client()
        user = c.login(username='testfile', password='testfile')
        self.assertEqual(user, True)
        
        self.result = get_next_question_or_none(self.u)
        self.assertNotEqual(self.result, None)

    #def test_parse_rule(self):
    #   parse_rule("ans1 : rec1", request)

    def tearDown(self):
        self.u.delete()
        self.q.delete()
        self.q2.delete()
        self.a.delete()
        self.a2.delete()
        self.p.delete()
        self.up.delete()
        self.qp.delete()

'''
# Stephen Lowry
class AnonPagesTest(unittest.TestCase):
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
          self.q.delete()'''

'''
class UserPagesTest(unittest.TestCase):
    def testUserPages(self):
        client = Client()
        self.u = User.objects.create_user(username='test', email="test@test.com", password='test')
        self.u.is_staff = False
        self.p = Profile.objects.create(name="Default")
        self.up = UserProfile.objects.create(user=self.u, profile=self.p)
        client.login(username='test', password='test')
        self.q = Question.objects.create(question = "Huh?")
        #home = client.get('/hello')
        #questions = client.get('/questions/')
        profile = client.get('/profile/')
        changeprofile = client.get('/changeprofile/')
        question = client.get('/questions/1/')
        answer = client.get('/questions/1/answer/')
        logout = client.post('/accounts/logout/')
        self.assertEqual(home.status_code, 200)
        #self.assertEqual(questions.status_code, 200)
        self.assertEqual(profile.status_code, 200)
        self.assertEqual(changeprofile.status_code, 200)
        self.assertEqual(question.status_code, 200)
        self.assertEqual(answer.status_code, 200)
        self.assertEqual(logout.status_code, 302) #redirected to home
    def tearDown(self):
        self.q.delete()
        self.u.delete()
        self.p.delete()
        self.up.delete()

class maintenance_test(unittest.TestCase):
    def maintenance_group_tests(self):
        client = Client()
        self.u = User.objects.create_user(username='test', email="test@test.com", password='test')
        self.u.is_staff = True
        # maintenance_group_edit_profiles()
        self.p = Profile.objects.create(name="Default")
        self.up = UserProfile.objects.create(user=self.u, profile=self.p)
        client.login(username='test', password='test')
        self.assertEqual(self.p, "Default")
        # maintenance_group_edit_profiles()
        self.p.name = "Manager"
        self.assertEqual(self.p, "Manager")
        # maintenance_group_add_question_path_to_profiles()
        self.q1 = Question.objects.create(question="how?")
        self.q2 = Question.objects.create(question="what?")
        self.q3 = Question.objects.create(question="when?")
        self.qp = QuestionPath(profile=self.p, current_question=self.q1, follow_question=self.q2)
        self.assertEquals(self.qp.profile, "Manager")
        self.assertEquals(self.qp.current_question, "how?")
        self.assertEquals(self.qp.follow_question, "what?")
        # maintenance_group_edit_question_path_for_profiles()
        self.qp.follow_question = self.q3
        self.assertEquals(self.qp.follow_question, "when?")
    def tearDown(self):
        self.q1.delete()
        self.q2.delete()
        self.q3.delete()
        self.u.delete()
        self.p.delete()
        self.qp.delete()
        self.up.delete()

'''

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

# Stephen lowry
class QuestionPathTest(unittest.TestCase):
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
class RecommendationTest(unittest.TestCase):
    def setUp(self):
        self.r = Recommendation.objects.create(recommendation="This is a recommendation")
    def testRecommendation(self):
        self.assertEqual(self.r.recommendation, "This is a recommendation")
    def tearDown(self):
        self.r.delete()


#Stephen Murphy
#Testing the recommendation parsing
class recParsing(unittest.TestCase):
    def setUp(self):
        self.link = Recommendation.objects.create(link="http://www.yahoo.com")
        self.text = Recommendation.objects.create(tex="Hello")
        self.yout = Recommendation.objects.create(you="<iframe width=\"560\" height=\"315\" src=\"http://www.youtube.com/embed/SBh01XZHfL0\" frameborder=\"0\" allowfullscreen></iframe>")
    def linkify(self):
        self.assertEqual(rec.media(self.link.link,0),"<a href=\"http://yahoo.com\">link</a>")
    def textTest(self):
        self.assertEqual(rec.media(self.text.tex,0),"Hello")
    def youTube(self):
        self.assertEqual(rec.media(self.yout.you,0),"<iframe width=\"560\" height=\"315\" src=\"http://www.youtube.com/embed/SBh01XZHfL0\" frameborder=\"0\" allowfullscreen></iframe>")

#Stephen Murphy
#Testing the parsing for rules
class ruleParsing(unittest.TestCase):
    def setUp(self):
	self.rule = "ans1 and ans2 : rec1"
    def parse(self):
	self.assertEqual(parse_rule(self.rule,context),"rec1")
	
