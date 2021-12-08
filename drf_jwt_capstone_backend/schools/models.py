from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.



class School(models.Model):
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
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    school_type = models.CharField(max_length=50, null=True, blank=False, unique=True, default='', choices=TYPE)
    school_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    school_description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    number_Reviews = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True )

    def __str__(self):
        return self.school_name

    


    
    
    
    