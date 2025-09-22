from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctorpage, name= 'doctors'),
    path('doctor/dr.saravanan_gobinathan/', views.drgobinathan, name='dr_gobinathan'),
    path('doctor/dr.chandrakala/', views.drchadrakala, name= 'dr_chadrakala'),
] 