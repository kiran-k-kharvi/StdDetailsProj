from django.db.models import fields
from django.db.models.base import Model
from django import forms
from .models import portfolio,student_Info
class student_details_form(forms.ModelForm):
    class Meta:
        model = student_Info
        fields = ('First_Name','Last_Name','Email','Password')
        widgets = {
            'First_Name': forms.TextInput(attrs={'placeholder': 'First Name',}),
            'Last_Name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'Password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

class portfolio_form(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ('gitLink','profile_pic')
        widgets = {
            'gitLink': forms.URLInput(attrs={'placeholder': 'GitHub Link'}),
        }