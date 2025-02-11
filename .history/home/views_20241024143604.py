from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, Phone=Phone, desc=desc, date=datetime.today())
        contact.save()
       
        def __str__(self):
            return self.name
        
    return render(request, 'contactus.html')