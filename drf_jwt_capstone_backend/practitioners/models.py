from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
# from django.utils import module_loading
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.


class Practitioner(models.Model):
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
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    middle_initial=models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    school_interest = models.CharField(max_length=50, null=True, blank=False, unique=True, default='', choices=TYPE)

    # def __str__(self):
    #     return self.user

    