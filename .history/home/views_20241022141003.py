from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return render(request, 'index.html')
    # return HttpResponse("This is Muhammad Yahya Rizwan")

def about(request):
    return HttpResponse("This is ABout page")
    
def services(request):
    return HttpResponse("this is services Page")

def contactus(request):
    return HttpResponse("Contact Details") 
