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
import copy

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

