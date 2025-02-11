from django.shortcuts import render
from .ca import carousel_img

def home(request):
    carousel_images = carousel_img.objects.all()
    return render(request, 'home.html', {'carousel_images': carousel_images})
