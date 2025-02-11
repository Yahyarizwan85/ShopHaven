from django.contrib import admin
from django.urls import path
from store import views as home
from home.views.login import Login
from home.views.signup import Signup
from 
urlpatterns = [
    path("", index, name='home'),
    path("about", home.about, name='about'),
    path("clothes", home.clothes, name='clothes'),
    path("contactus", home.contactus, name='contactus'),
    path("signup", Signup.as_view(), name='signup'),
    path("login", Login.as_view(), name='login'),
]
