
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth import authenticate, login
from django.test.client import Client
import re
from django.contrib.auth.models import User
from auth.models import *
from questions.models import *
from recommendations.models import *
from django.test import TestCase

#Stephen Murphy
#regular expressions returning HTML tags in a list for comparison
def getRegEx(reg,string):
        p = re.compile(reg)
        result = p.findall(str(string))
        return result


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#Stephen Murphy
#test if recommendations are stored and retrieved correctly
class RecommendationsTest(TestCase):
    def setUp(self):
        self.rec = Recommendation.objects.create(recommendation="this")
        
#    def test_presence(self):
#        self.assertEqual(Recommendation.objects.all().get().recommendation,str(self.rec))

class UploadTest(TestCase):
	def setUp(self):
		self.upload = UploadedFile.objects.create(files="hello.txt")
		self.client = Client()
	def testPresence(self):
		self.assertIn(self.upload,UploadedFile.objects.all(),"hello.txt")

#Stephen Murphy
#test if markdown syntax is converting to HTML
#class MarkupTest(TestCase):
#    def setUp(self):
#        self.link = Recommendation.objects.create(name="r1",recommendation="[link](http://link.com)")
#        self.bold = Recommendation.objects.create(name="r2",recommendation="<b>bold</b>")
#        self.ital = Recommendation.objects.create(name="r3",recommendation="<i>italics</i>")
#        self.h2 = Recommendation.objects.create(name="r4",recommendation="## big letters ##")
#        self.img = Recommendation.objects.create(name="r5",recommendation="![](http://someurl.com/i.jpg)")
#	self.profile = Profile.objects.create(name="default")
#        self.client = Client()
#	self.user = User.objects.create_user("john smith","password")
#	self.userProf = UserProfile.objects.create(user=self.user,profile=self.profile)
#	self.user.save()
#
#	self.question1 = Question.objects.create(question = "?")
#	self.answer1 = Answer.objects.create(question=self.question1,answer = "yes")
#	self.ansQ1 = AnsweredQuestion.objects.create(user=self.user,question=self.question1,answer = self.answer1)
#
#	self.question2 = Question.objects.create(question = "??")
#	self.answer2 = Answer.objects.create(question=self.question2,answer = "yes")
#	self.ansQ2 = AnsweredQuestion.objects.create(user=self.user,question=self.question2,answer = self.answer2)
#
#	self.questionpath = QuestionPath.objects.create(profile=self.profile,current_question=self.question1,follow_question=self.question2)
#	
##    def testMark(self):
##        page = self.client.get("/index/")
##        self.assertEqual(page.status_code,200)
##
#    def test_link(self):
#	self.client.login(username="john smith",password="password")
#	self.client.post("/accounts/login/")
#	profileRec = RecommendationProfile.objects.create(recommendation=self.link,profile=self.profile)
##	login(request,self.user)
#	answerlink = RecAnswerLink.objects.create(question=self.question1,recommendation=self.link,answer=self.answer1)
#        page = self.client.get("/index/")
#        reg = "<a href=\"http://link.com\">"
#        self.assertIn(reg,getRegEx(reg,page))
#
#    def test_bold(self):
#	profileRec = RecommendationProfile.objects.create(recommendation=self.bold,profile=self.profile)
##	login(request,self.user)
#	answerlink = RecAnswerLink.objects.create(question=self.question1,recommendation=self.bold,answer=self.answer1)
#        page = self.client.get("/index/")
#        reg = "<b>bold</b>"
#        self.assertIn(reg,getRegEx(reg,page))
#
#    def test_ital(self):
#	profileRec = RecommendationProfile.objects.create(recommendation=self.ital,profile=self.profile)
##	login(request,self.user)
#	answerlink = RecAnswerLink.objects.create(question=self.question1,recommendation=self.ital,answer=self.answer1)
#        page = self.client.get("/index/")
#        reg = "<i>italics</i>"
#        self.assertIn(reg,getRegEx(reg,page))
#
#    def test_h2(self):
#	profileRec = RecommendationProfile.objects.create(recommendation=self.h2,profile=self.profile)
##	login(request,self.user)
#	answerlink = RecAnswerLink.objects.create(question=self.question1,recommendation=self.h2,answer=self.answer1)
#        page = self.client.get("/index/")
#        reg = "<h2>big letters</h2>"
#        self.assertIn(reg,getRegEx(reg,page))
#
#    def test_img(self):
#	profileRec = RecommendationProfile.objects.create(recommendation=self.img,profile=self.profile)
##	login(request,self.user)
#	answerlink = RecAnswerLink.objects.create(question=self.question1,recommendation=self.img,answer=self.answer1)
#        page = self.client.get("/index/")
#        reg = "<img alt=\"\" src=\"http://someurl.com/i.jpg\" />"
#        self.assertIn(reg,getRegEx(reg,page))

