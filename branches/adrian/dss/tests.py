"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test.client import Client
from django.test import TestCase


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/hello_world/')
        self.assertEqual(response.status_code, 200)
       


   
