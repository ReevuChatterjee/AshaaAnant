from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rescue/',views.rescue,name='rescue'),
    path('submit-rescue/', views.submitRescueReport, name='submitRescue'),
    path('adoption/',views.adoption,name='adoption'),
    path('donate/',views.donate,name='donate'),
    path('volunteer/',views.volunteer,name='volunteer'),
    path('view-complaints/', views.view_complaints, name='view_complaints'),
    path('stafflogin/',views.login_view,name='stafflogin'),
    path('staffsignup/',views.signup,name='staffsignup'),
    path('logout/', views.logout_view, name='logout'),
    path('export-pdf/', views.export_complaints_pdf, name='export_pdf'),

]
