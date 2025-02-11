

from django.shortcuts import render
from .models import CarouselImg

def home(request):
    carousel_images = CarouselImg.get_all_carousel()
    return render(request, 'home.html', {'carousel_images': carousel_images})
