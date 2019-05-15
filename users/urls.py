# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('profile/', views.Profile, name='profile'),
]