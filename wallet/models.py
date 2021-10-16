from django.db import models
from accounts.models import User

# Create your models here.

class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    balance = models.CharField(max_length=20,)
