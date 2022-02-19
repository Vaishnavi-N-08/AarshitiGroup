from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),  
    path('register', views.register,name="register"),  
    path('logout', views.logout,name="logout"),  
    path('feedback', views.feedback,name="feedback"),  
    path('spices', views.spices,name="spices"),  
    path('agrotech', views.agrotech,name="agrotech"),  
    path('construction', views.construction,name="construction"),    
]