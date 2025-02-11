from django.shortcuts import render, HttpResponse

# Create your views here.
def index(reque):
    return HttpResponse("this is homepage")
    