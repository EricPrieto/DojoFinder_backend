from django.urls import path
from .views import PractitionerList
from schools import views
from .import views

urlpatterns = [
    path('', views.PractitionerList.as_view()),
   
]