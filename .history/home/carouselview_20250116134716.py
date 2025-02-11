from django.shortcuts import render
from .carousel import carousel_img

def carousel_(request):
    carousel_images = carousel_img.objects.all()
    return render(request, 'home.html', {'carousel_images': carousel_images})
