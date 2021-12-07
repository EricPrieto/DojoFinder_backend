from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Practitioner(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    middle_initial=models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    school_interest = models.CharField(max_length=200)