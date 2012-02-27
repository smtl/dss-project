
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
import re

from dss.recommendations.models import Recommendation
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
        
    def test_presence(self):
        self.assertEqual(Recommendation.objects.all().get().recommendation,str(self.rec))


#Stephen Murphy
#test if markdown syntax is converting to HTML
class MarkupTest(TestCase):
    def setUp(self):
        self.link = Recommendation.objects.create(recommendation="[link](http://link.com)")
        self.bold = Recommendation.objects.create(recommendation="<b>bold</b>")
        self.ital = Recommendation.objects.create(recommendation="<i>italics</i>")
        self.h2 = Recommendation.objects.create(recommendation="## big letters ##")
        self.img = Recommendation.objects.create(recommendation="![](http://someurl.com/i.jpg)")
        self.client = Client()

    def testMark(self):
        page = self.client.get("")
        self.assertEqual(page.status_code,200)

    def test_link(self):
        page = self.client.get("")
        reg = "<a href=\"http://link.com\">"
        self.assertIn(reg,getRegEx(reg,page))

    def test_bold(self):
        page = self.client.get("")
        reg = "<b>bold</b>"
        self.assertIn(reg,getRegEx(reg,page))

    def test_ital(self):
        page = self.client.get("")
        reg = "<i>italics</i>"
        self.assertIn(reg,getRegEx(reg,page))

    def test_h2(self):
        page = self.client.get("")
        reg = "<h2>big letters</h2>"
        self.assertIn(reg,getRegEx(reg,page))

    def test_img(self):
        page = self.client.get("")
        reg = "<img alt=\"\" src=\"http://someurl.com/i.jpg\" />"
        self.assertIn(reg,getRegEx(reg,page))
