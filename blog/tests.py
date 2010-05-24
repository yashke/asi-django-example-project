"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Post

class PostStrTest(TestCase):
    def setUp(self):
        self.post = Post()

    def testWithTitle(self):
        self.post.title = "kaka"
        self.assertEqual(str(self.post), "Post: kaka")

    def testWithoutTitle(self):
        self.assertEqual(str(self.post), "Post: untitled")
