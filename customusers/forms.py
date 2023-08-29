from django import forms
from .models import CustomUsers
from django.core.exceptions import ValidationError

# https://stackoverflow.com/questions/63539321/how-to-check-password-against-previously-used-passwords-in-django
class FormUser(forms.ModelForm):
    class Meta:
        model = CustomUsers
        fields = ['username', 'email' ,'phone_number', 'first_name','last_name' , 'profile_image', 'password','re_password']


