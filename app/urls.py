from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rescue/',views.rescue,name='rescue'),
    path('submit-rescue/', views.submitRescueReport, name='submitRescue'),
    path('adoption/',views.adoption,name='adoption'),
    path('donate/',views.donate,name='donate'),
    path('volunteer/',views.volunteer,name='volunteer'),
]
