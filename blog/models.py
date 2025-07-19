from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog_images/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes= models.IntegerField(default=0)

    def __str__(self):
        return self.title

    