from django.db import models
from django.db.models.base import Model

# Create your models here.


class School(models.Model):
    user = models.ForeignKey('authentication.User', blank=True, null=True, on_delete=models.CASCADE)
    school_type = models.CharField(max_length=25)
    school_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    school_description = models.CharField(max_length=200)
    
    
    
    
    