from django.contrib import admin
from home.models import Contact, Product, Category, Customer, Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)