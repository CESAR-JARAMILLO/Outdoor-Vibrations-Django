from django.db import models
from django.db.models import ImageField

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    image = ImageField(upload_to='images/')
