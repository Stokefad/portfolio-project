from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(upload_to="imagesblog/")
