from django.shortcuts import render, HttpResponse

# Create your views here.
def index(re):
    return HttpResponse("this is homepage")
    