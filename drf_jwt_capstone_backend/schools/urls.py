from django.urls import path
from .views import SchoolList
from schools import views
from .import views

urlpatterns = [
    path('', views.SchoolList.as_view()),
    path('', views.ReviewList.as_view()),

]