from django import forms
from .models import *
from django.contrib.auth.forms  import AuthenticationForm
from django_summernote.widgets import SummernoteWidget



class login_form(AuthenticationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'username','placeholder':'Enter Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'username','placeholder':'Enter Password'}))


class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ['caption', 'image','description','is_show_on_home_page']


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = [
            'title', 'location', 'vacancy', 'desired_qualification',
            'experience_required', 'career_description', 'roles_responsibility', 'skills_required','is_publish'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}), 
            'vacancy': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience_required': forms.TextInput(attrs={'class': 'form-control'}), 
            
            'desired_qualification': forms.Textarea(attrs={'class': 'summernote form-control', 'data-height': '100'}),
            'career_description': forms.Textarea(attrs={'class': 'summernote form-control', 'data-height': '300'}),
            'roles_responsibility': forms.Textarea(attrs={'class': 'summernote form-control', 'data-height': '200'}),
            'skills_required': forms.Textarea(attrs={'class': 'summernote form-control', 'data-height': '200'}),
            
            'is_publish': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left:10px;'}),

        }