from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"


class TweetPic(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='pics/')

    def __str__(self):
        return f"Photo for tweet {self.tweet.id}"

    class Meta:
        verbose_name = "Tweet Photo"
        verbose_name_plural = "Tweet Photos"
