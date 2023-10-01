from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null =True)
    email = models.EmailField(unique=True)
    dob = models.DateField( null=True,blank=True, default=datetime.date.today)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]