from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship,name="scholarship"),  
    path('counselling', views.counselling,name="counselling"),
]