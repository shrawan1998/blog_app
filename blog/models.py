from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
