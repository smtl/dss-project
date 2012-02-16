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
"""from signedcookies import middleware"""
"""from middleware import SimpleCookiesMiddleware"""
from Cookie import SimpleCookie, Morsel
import copy

from django.conf import settings
from django.core.context_processors import csrf
from django.middleware.csrf import CsrfViewMiddleware
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
