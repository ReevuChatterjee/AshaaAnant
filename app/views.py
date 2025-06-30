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

def adoption(request):
    return HttpResponse("ADOPTION")

def donate(request):
    return HttpResponse("DONATE")

def volunteer(request):
    return HttpResponse("VOLUNTEER")
# Create your views here.
