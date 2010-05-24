"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import Post

class PostStrTest(TestCase):
    def setUp(self):
        self.post = Post()

    def testWithTitle(self):
        self.post.title = "kaka"
        self.assertEqual(str(self.post), "Post: kaka")

    def testWithoutTitle(self):
        self.assertEqual(str(self.post), "Post: untitled")

class ViewIndexTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post1 = Post(title="kaka", content="dudu")
        self.post1.save()
        self.post2 = Post(title="kuku", content="dada")
        self.post2.save()

    def testTemplate(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/index.html')

    def testPostList(self):
        response = self.client.get('/blog/')
        self.assertEqual(len(response.context['posts']), 2)
