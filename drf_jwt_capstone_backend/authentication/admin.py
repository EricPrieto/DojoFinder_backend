from django.contrib import admin


# from drf_jwt_capstone_backend.authentication.serializers import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.
admin.site.register(User)