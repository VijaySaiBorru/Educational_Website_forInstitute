from django.shortcuts import render
from app1.models import parent
from app1.forms import parentform
from app1.forms import contactform

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def about(request):
    return render(request,'app1/about.html')

def python(request):
    return render(request,'app1/python.html')

def java(request):
    return render(request,'app1/java.html')

def fullstack(request):
    return render(request,'app1/fullstack.html')

def photos(request):
    return render(request,'app1/photos.html')

def videos(request):
    return render(request,'app1/videos.html')

def parent(request):
    form=parentform()
    if request.method=='POST':
        form=parentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app1/parent.html',{'form':form})

def latest(request):
    return render(request,'app1/latest.html')

def contact(request):
    form=contactform()
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app1/contact.html',{'form':form})
