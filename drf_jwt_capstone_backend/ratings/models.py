from django.db import models
from enum import unique
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework_simplejwt.tokens import RefreshToken
# from .models import School
from django.db.models.fields.related import ManyToManyField


# Create your models here.

class Rating(models.Model):
    rated_school = ManyToManyField("schools.School", related_name="rtd_school_name")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # class Meta:
    #     unique_together = (('user', 'school_name'),)
    #     unique_together = (('user', 'school_name'),)
    


    # def no_of_ratings(self):
    #     ratings = Rating.objects.filter(school =self)
    #     return len(ratings)