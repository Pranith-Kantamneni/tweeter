from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='photos/', blank=True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'
