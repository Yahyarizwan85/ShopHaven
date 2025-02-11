from django.urls import path
from .views
 
urlpatterns = [
    path("", home.index, name='home'),
    path("about", home.about, name='about'),
    path("clothes", home.clothes, name='clothes'),
    path("contactus", home.contactus, name='contactus'),
    path("signup", Signup.as_view(), name='signup'),
    path("login", Login.as_view(), name='login'),
]
