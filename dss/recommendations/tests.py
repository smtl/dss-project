
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


