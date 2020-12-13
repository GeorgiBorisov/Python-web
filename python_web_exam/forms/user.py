from django import forms
from django.contrib.auth.models import User

class UsersForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    username = forms.CharField(min_length=3, max_length=20)
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
        
class UsersLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    
class EditUserForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, required=False)
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    class Meta:
        model = User
        fields = ['username', 'password']
       