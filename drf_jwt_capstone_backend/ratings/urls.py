from django.urls import path
from schools import views
from .import views
from .views import RatingView

urlpatterns = [
    path('', views.RatingView.as_view())

    ]
    