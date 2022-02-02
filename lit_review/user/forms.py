from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        exclude = ['username']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'})
        }

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }