from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.



class School(models.Model):
    TYPE =(
        ('AK', 'Aikido'),
        ('BX', 'Boxing'),
        ('BJJ', 'Brazilian Juijitsu'),
        ('CP', 'Capoeira'),
        ('KA', 'Karate'),
        ('KM', 'Krav Maga'),
        ('KF', 'Kung Fu'),
        ('KB', 'KickBoxing'),
        ('MT', 'Muay Thai'),
        ('TKD', 'Tae Kwon Do'),
        ('VT', 'Vale Tudo'),
        ('WR', 'Wrestling'),
        
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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.school_name

    

   

    

class Review(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    school =models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school, self.rating
    
    
    
    
    