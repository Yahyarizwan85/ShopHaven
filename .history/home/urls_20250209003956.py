from django.urls import path, include
from .views import homes
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import Check_out
from .views.orders import Orders
from home.middleware.logguard import auth_middleware


urlpatterns = [
    path("", homes.index, name='home'),
    path("about", homes.about, name='about'),
    path("shop", homes.Clothes.as_view(), name='clothes'),
    path("contact", homes.contact_us, name='contact'),
    path("signup", Signup.as_view(), name='signup'),
    path("login", Login.as_view(), name='login'),
    path("logout", logout , name='logout'),
    path("cart", Cart.as_view(), name='cart_Products'),
    path("check-out", Check_out.as_view(), name='chectout'),
    path("order", auth_middleware(Orders.as_view()), name='order'),
]
