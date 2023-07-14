from django.shortcuts import render
from .import views
from django.http import  HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'Contact.html')
def registration(request):
    if request.method=='POST':
        fname=request.POST.get('first')
        registration(ifirst_name=fname).sava()
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')


