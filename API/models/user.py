from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from requests.models import Response
from rest_framework import status


    
class User(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    password = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'password', 'birth_date']

    def __str__(self):
        return self.user_name

    