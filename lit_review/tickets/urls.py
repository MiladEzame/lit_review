from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('tickets/', views.tickets, name='tickets'),
    path('create_ticket/', views.createTicket, name='create_ticket'),
    path('tickets/<str:pk>/', views.show, name='ticket'),
    path('', views.dashboard)
]
