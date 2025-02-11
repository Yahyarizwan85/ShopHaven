from django.contrib import admin
from home.models import Contact, Product, Category
from .customer import Customer
from .order import Order 
from home.carousel import CarouselImg
from django.conf import settings
from django.conf.urls import static
 
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class CarouselImgAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image', 'Para')

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CarouselImg)