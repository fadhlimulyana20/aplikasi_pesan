from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    destination = models.CharField(max_length=100, null=False, default="destination")
