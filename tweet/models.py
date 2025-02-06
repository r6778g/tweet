from django.db import models
from django.utils.timezone import now

class Tweet(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    image = models.ImageField(upload_to='tweets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this field

    def __str__(self):
        return self.text
