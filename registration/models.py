from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profession = models.CharField(max_length=50, blank=True, null=True)
    institute = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(auto_now_add=False, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image_profile = models.ImageField(upload_to='images/profile/', default='images/profile/default/icons8-user-100.png')
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()