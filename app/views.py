from django.shortcuts import render,redirect
from .models import RescueDB,CustomUser
import uuid
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
import os
from weasyprint import HTML
from dotenv import load_dotenv
from django.conf import settings
load_dotenv()

ALLOWED_SIGNUP_IPS = os.getenv("ALLOWED_SIGNUP_IPS", "").split(",")
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # Handles multiple IPs (first is original client)
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    return render(request,'home.html')

def rescue(request):
    return render(request,'rescue.html')

def logout_view(request):
    logout(request)
    return redirect('stafflogin')

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

def export_complaints_pdf(request):
    reports = RescueDB.objects.all()
    html_string = render_to_string('export_pdf_template.html', {
        'reports': reports,
        'MEDIA_ROOT': settings.MEDIA_ROOT,
        'MEDIA_URL': settings.MEDIA_URL,
        'BASE_DIR': settings.BASE_DIR,
        'request': request,  # for absolute URIs
    })

    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="complaints_report.pdf"'
    return response

@login_required(login_url='stafflogin')
def view_complaints(request):
    reports = RescueDB.objects.all().order_by('-timestamp')
    return render(request, 'view_complaints.html', {'reports': reports})


def adoption(request):
    return render(request,'adoption.html')

def donate(request):
    return render(request,'donation.html')

def volunteer(request):
    return render(request,'volunteer.html')

def login_view(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user_obj=CustomUser.objects.get(email=email)
            username=user_obj.username
        except CustomUser.DoesNotExist:
            messages.error(request,"Invalid email or password")
            return redirect('login_view')
        
        user=authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('view_complaints')
        else:
            messages.error(request,"Invalid email or password")
            return redirect('login_view')

    return render(request,'login.html')

def signup(request):
    client_ip = get_client_ip(request)
    if client_ip not in ALLOWED_SIGNUP_IPS:
        return HttpResponseForbidden(f"Access denied. Detected IP: {client_ip}. You are not allowed to access this page.")
    if request.method=="POST":
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpass=request.POST.get('confirm-password')
        username = email.split('@')[0] + "_" + str(uuid.uuid4())[:8]
        user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=fname,
                last_name=lname,
                is_staff=True
            )
    return render(request,'signup.html')
# Create your views here.
