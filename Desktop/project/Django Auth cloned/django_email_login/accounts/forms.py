from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        "type": "email",
        "placeholder": "Email",
        "class": "form-control mb-3"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
       "type": "text",
        "placeholder": "Username",
        "class": "form-control mb-3" 
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Password",
        "class": "form-control mb-3" 
    }))
    password2 =  forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Confirm Password",
        "class": "form-control mb-3" 
    }))
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=(forms.TextInput(attrs={
        "type": "email",
        "placeholder": "Email",
        "class": "form-control mb-3" 
    })))
    password = forms.CharField(label='Password', widget=(forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Password",
        "class": "form-control mb-3" 
    })))
