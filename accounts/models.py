from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    individual = models.CharField(max_length=30, blank = True, null = True)
    business = models.CharField(max_length=30, blank = True, null = True)
    fullname = models.CharField(max_length=50)
    referral_code = models.CharField(max_length=10,blank = True, null = True,)
    phone_number = models.CharField(max_length=20, blank=False, null=False)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
