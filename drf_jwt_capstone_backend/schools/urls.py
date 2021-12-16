from django.urls import path
from .views import SchoolList
from schools import views
from .import views
# from .views import RatingView

urlpatterns = [
    path('schools/', views.SchoolList.as_view()),
    # path('', views.RatingView.as_view()),
    

]