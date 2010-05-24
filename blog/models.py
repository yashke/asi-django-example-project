from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        if self.title and len(self.title):
            return "Post: %s" % (self.title, )
        else:
            return "Post: untitled"
