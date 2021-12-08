from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from django.db.models.base import Model
from.models import School

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    school_name = models.ForeignKey(School, blank=True, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school_name , self.rating
    