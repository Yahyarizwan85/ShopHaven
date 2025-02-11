from django.contrib import admin
from django.urls import path
from .views import home, login, signup
from home.views.login import  Login
from home.views.signup import Signup

urlpatterns = [
    path("",home.index, name='home'),
    path("about",home.about, name='about'),
    path("clothes",home.clothes, name='clothes'),
    path("contactus",home.contactus, name='contactus'),
    path("signup", signup.Signup.as_view(), name='signup'),
    path("login", login.Login.as_view(), name='login'),

]
