from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserData


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    email = forms.CharField(label='Email Address', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 
            'password2',
        ]


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'An account with this email address already exists.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password can not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

class UserDataForm(forms.ModelForm):
    address_1=forms.CharField(label="Address Line 1")
    address_2=forms.CharField(label="Address Line 2", required=False)
    postal_code=forms.CharField(label="Postal Code")
    town_or_city=forms.CharField(label="Town or City")
    country=forms.CharField(label="Country")
    class Meta:
        model=UserData
        fields=[
            'address_1', 
            'address_2', 
            'postal_code', 
            'town_or_city', 
            'state_or_province', 
            'country',
        ]
        