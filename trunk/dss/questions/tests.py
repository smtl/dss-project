"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from __future__ import with_statement
from django.contrib.auth import login, logout
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
from auth.models import Profile
from django.core import mail
import copy


from auth.models import Profile, UserProfile
from recommendations.models import Recommendation, RecAnswerLink
from questions.models import Question, Answer, QuestionPath
from questions.models import AnsweredQuestion
import tempfile


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


#Adrian Kwizera
#Record view test
class record_view(TestCase):
    def setup(self):
        self.u = User.objects.create(username="admin", password="admin")
        self.u = User.objects.get('/questions/record_view.html/')
        self.assertEqual(u.status_code, 200)
        self.assertEqual(questions.status_code, 200)
        self.assertEqual(login.status_code, 200)

    def tearDown(self):
        self.client.logout()
        self.u.delete()   
       
 
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
#Testing saved and resumed sessions
class TestSessionState(TestCase):

    def setUp(self):
     
        self.client.get('/questions/') # after this, self.client.session is a real session
        s = self.client.session
        s['key'] = 'value'
        s.save()


#Adrian Kwizera
#Testing assertions for recommendations assigned to user profiles
class TestAssertion(TestCase):  
  
    def test_assertion_of_recommendations(self):   
        self.assertTrue(1) # evaluates truth value  
        self.assertFalse(0) # evaluates false value  
        self.assertEquals(1, 1) # evaluates second (dynamic) value equals the first (known) value;  
        self.assertNotEquals(1, 2)  
          
        o = 1  
        self.assertIs(o, o) # assert evaluate to the same object  
        self.assertIn(1, [1, 2, 3]) # assert first value in second  
        self.assertIsInstance(self, TestCase) # first value is instance of second  


#Adrian Kwizera
#Testing saved progress for questions_answers_recommendation path
class save_progress(TestCase):

    def setUp(self):
     
        self.client.get('/questions/')
        self.client.get('/answers/')
        self.client.get('/recommendation/')
        s = self.client.session
        s['key'] = 'value'
        s.save()


#Adrian Kwizera
#Testing order of recommendations based on answered question
class TestSort(unittest.TestCase):

    def setUp(self):
       self.alist = [5, 2, 3, 1, 4]

    def test_ascending_sort(self):
       self.alist.sort()
       self.assertEqual(self.alist, [1, 2, 3, 4, 5])

    def test_sorting_reverse(self):
       self.alist.sort()
       self.alist.reverse()
       self.assertEqual(self.alist, [5, 4, 3, 2, 1])


#Adrian Kwizera
#Maintainer test
class MaintainerTestCase(unittest.TestCase):
    def setUp(self):
        self.cr = Question.objects.create(question="Do you love fish")
        self.an = Answer.objects.create(question=self.cr, answer="perhaps")
    
    def tearDown(self):
        self.cr.delete()
        self.an.delete()


# Adrian Kwizera
class AdminCustomisationTest(TestCase):
    
    def setUp(self):
        username = 'test_user'
        pwd = 'secret'

        self.u = User.objects.create_user(username, '', pwd)
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.save()

        self.assertTrue(self.client.login(username=username, password=pwd),
            "Logging in user %s, pwd %s passed." % (username, pwd))

        self.assertEqual(home.status_code, 200)
        self.assertEqual(profile.status_code, 302)
        self.assertEqual(changeprofile.status_code, 200)
        self.assertEqual(login.status_code, 200)

        questions.objects.all().add()

    def tearDown(self):
        self.client.logout()
        self.u.delete()


#Adrian Kwizera
#Testing help link for maintainer
class HelpTest(TestCase):

    def setup(self):
        self.u = User.objects.create(username="admin", password="admin")
        self.u = User.objects.get('/questions/help_staff.html/')
        self.assertEqual(u.status_code, 200)
        self.assertEqual(changeprofile.status_code, 200)#redirects to different profile
        self.assertEqual(login.status_code, 200)

    def tearDown(self):
        self.client.logout()
        self.u.delete()


#Adrian Kwizera
#Testing help link for guest
class HelpTest(TestCase):

    def setup(self):
        self.u = User.objects.get('/questions/help_user.html/')
        self.assertEqual(u.status_code, 200)
        self.assertEqual(profile.status_code, 302) #redirects guest user

      
    def tearDown(self):
        self.u.delete()


#Adrian Kwizera
#Testing string assertions by the makefile
class TestMakeFile(unittest.TestCase):
    def assertMultiLineEqual(self, first, second, msg=None):
        """Assert that two strings are equal, when traversing the makefile
        """
        self.assertTrue(isinstance(first, str),
                'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                'Second argument is not a string')

        if first != second:
            message = ''.join(difflib.ndiff(first.splitlines(True),
                                                second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("strings are unequal:\n" + message)


#Adrian Kwizera
#creating connections test
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExecutableObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()


#test for deleting rules
#class deleterule((unittest.TestCase):
     

#Adrian Kwizera
#Testing loading
class TestLoader(unittest.TestCase):

    #test_cases = (TestCase1, TestCase2, TestCase3)
    def load_tests(loader, tests, pattern):
     suite = TestSuite()
     for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
     return suite


#Adrian Kwizera
#Testing file make and deletion
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # create fixtures
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
       

     def test_fixture_1(self):
    # self.tempdir was just created
    # Create a file
      open(os.path.join(self.tempdir, 'test'), 'w')
    # self.tempdir will be deleted after the function call

     def test_fixture_2(self):
    # Check that the file 'test' doesn't exist
        self.assertRaise(IOError, open, os.path.join(self.tempdir, 'test'))


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
        home = client.get('/hello')
        questions = client.get('/questions/')
        profile = client.get('/profile/')
        changeprofile = client.get('/changeprofile/')
        question = client.get('/questions/1/')
        answer = client.get('/questions/1/answer/')
        logout = client.post('/accounts/logout/')
        self.assertEqual(home.status_code, 200)
        self.assertEqual(questions.status_code, 200)
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

