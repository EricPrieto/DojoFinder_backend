from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
   
   
    TYPE =(
        ('Aikido', 'Aikido'),
        ('Boxing', 'Boxing'),
        ('BJJ', 'Brazilian Juijitsu'),
        ('Capoeira', 'Capoeira'),
        ('Karate', 'Karate'),
        ('KravMaga', 'Krav Maga'),
        ('KungFu', 'Kung Fu'),
        ('KickBoxing', 'KickBoxing'),
        ('MuayThai', 'Muay Thai'),
        ('TaeKwon Do', 'Tae Kwon Do'),
        ('ValeTudo', 'Vale Tudo'),
        ('Wrestling', 'Wrestling'),
        
    )
   
    middle_name = models.CharField(max_length=20)
    address = models.TextField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=12, null=True)
    school_interest = models.CharField(max_length=50, null=True, blank=False, unique=True, choices=TYPE)

