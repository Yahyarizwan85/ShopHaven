from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Muhammad Yahya Rizwan")

def about(request):
    return render(request, 'About.html')
    return HttpResponse("This is ABout page")
    
def services(request):
    return render(request, 'servies.html')
    return HttpResponse("this is services Page")

def contactus(request):
    return render(request, 'contactus')
    return HttpResponse("Contact Details") 
