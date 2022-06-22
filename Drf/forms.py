from pyexpat import model
from django import forms
from .models import blogmodel


class apiform(forms.ModelForm):
    class Meta:
        model = blogmodel
        fields = ['wrtier','title','body']



# class Contactform(forms.ModelForm):
#     name=forms.CharField()
#     message=forms.CharField(widget={forms.Textarea})
#     def send_email(self):
#         pass
    