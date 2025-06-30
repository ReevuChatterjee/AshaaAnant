from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'home.html')

def rescue(request):
    return render(request,'rescue.html')

# Create your views here.
