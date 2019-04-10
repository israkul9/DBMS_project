from django import forms
from django.contrib.auth.models import User
from main_app.models import *


class Createu(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}),required = True,max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first_name'}),required=True,max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name'}),required=True,max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
                            required=True, max_length=50)

    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','password']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )