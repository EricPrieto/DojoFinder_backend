from django.contrib.auth import get_user
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model
User = get_user_model()

# from drf_jwt_capstone_backend.authentication.serializers import User
from .views import RegisterView, UserDetail, UserList


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('userid/', UserList.as_view(), name="userlist"),
    path('user/<int:pk>', UserDetail.as_view(), name='getuser'), #https://127.0.0.1.8000/api/auth/user
    path('username/<str:username>', UserDetail.as_view(), name='get_user_by_name'),
    
]
