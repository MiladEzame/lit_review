from django.forms import ModelForm
from .models import Ticket
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'})
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }