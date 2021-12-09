# from django.contrib import admin
# from django.contrib.admin.filters import ListFilter
from django.db import models
from django.db.models.fields.related import ManyToManyField
# from django.db.models.base import Model
# from .models import School

from django.contrib.auth import get_user_model
User = get_user_model()

# from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    school_name = ManyToManyField("schools.School", related_name="rvw_school_name")
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school_name , self.rating


    