from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/<str:pk>/', views.show, name='user')
]
