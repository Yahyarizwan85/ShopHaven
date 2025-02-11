from django.contrib import admin
from .models import CarouselImg

@admin.register(CarouselImg)
class CarouselImgAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image', 'Para')
