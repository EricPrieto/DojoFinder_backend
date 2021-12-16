from enum import unique
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.http import response
User = get_user_model()
from django.core.validators import MaxValueValidator, MinValueValidator
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
    school_address = models.CharField(max_length=50)
    school_zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    school_description = models.TextField(null=True, blank=True)
    # rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # number_Reviews = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True )

    def __str__(self):
        return self.school_name

    
    # def no_of_ratings(self):
    #     ratings = Rating.objects.filter(school =self)
    #     return len(ratings)

    # def avg_rating(self):
    #     sum = 0
    #     ratings = Rating.objects.filter(school =self)
    #     for rating in ratings:
    #         sum += rating.stars

    #     if len(ratings) > 0:
    #         return sum / len(ratings)
    #     else:
    #         return 0


# class Rating(models.Model):
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     return self.school

    # class Meta:
    #     unique_together = (('user', 'school'),)
    #     unique_together = (('user', 'school'),)
    



   
    


    
    
    
    