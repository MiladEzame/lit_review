from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('tickets/', views.tickets, name='tickets'),
    path('create_ticket/', views.createTicket, name='create_ticket'),
    path('dashboard/<int:ticket_id>', views.createReview, name='create_review'),
    path('update_ticket/<str:pk>/', views.updateTicket, name='update_ticket'),
    path('delete_ticket/<str:pk>/', views.deleteTicket, name='delete_ticket'),
    path('tickets/<str:pk>/', views.show, name='ticket'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/<str:pk>/', views.show_user, name='show_user'),
    path('', views.dashboard)
]
