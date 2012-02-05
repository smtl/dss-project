"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class HelloTestCase(unittest.TestCase):
    def testHello(self):
        client = Client()
        response = client.get('/hello/?name=stephen')
        self.assertEqual(response.status_code, 200)
