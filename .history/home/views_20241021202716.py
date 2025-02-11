from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Muhammad Yahya Rizwan")

def about(request):
    return HttpResponse("This is ABout page")
    
def services(request):
def contactus(request):
    return HttpResponse("Contact Details") 

    return HttpResponse("this is services Page")