from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Blogpostmodel(models.Model):
    title = models.CharField(max_length=200, null=True,blank=True)
    content = models.CharField(max_length=5000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
    


class Comment(models.Model):
    post = models.ForeignKey('Blogpostmodel', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text