from django.urls import path
from .views import ReviewList
from schools import views
from .import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),

]