from django.shortcuts import render, HttpResponse,redirect
from .models import RescueDB

def home(request):
    return render(request,'home.html')

def rescue(request):
    return render(request,'rescue.html')

def submitRescueReport(request):
    if request.method=="POST":
        contactName=request.POST.get('contactName')
        contactNumber=request.POST.get('contactNumber')
        address=request.POST.get('address')
        type=request.POST.get('animalType')
        photo=request.FILES.get('photo')
        issue=request.POST.get('issue')
        en=RescueDB(contactName=contactName,contactNumber=contactNumber,location=address,type=type,photo=photo,issueFaced=issue)
        en.save()
        return render(request, 'rescue.html', {'success': True})
    
    return redirect('rescue')

def view_complaints(request):
    reports = RescueDB.objects.all().order_by('-timestamp')
    return render(request, 'view_complaints.html', {'reports': reports})

def adoption(request):
    return render(request,'adoption.html')

def donate(request):
    return render(request,'donation.html')

def volunteer(request):
    return render(request,'volunteer.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
# Create your views here.
