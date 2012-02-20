"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from dss.recommendations.models import Recommendation
from django.test import TestCase


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
