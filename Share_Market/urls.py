from django.urls import path
from . import views

urlpatterns = [
    path('',views.stocks, name='stocks'),
    path('company/', views.company, name ='company')
]