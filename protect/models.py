from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OneTimeCode(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE,unique=False)
    code = models.CharField(max_length = 32)
