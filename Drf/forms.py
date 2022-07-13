from django import forms
from .models import blogmodel


class apiform(forms.ModelForm):
    phone_number = forms.RegexField(regex=r'^(\+98|0)?9\d{9}$')
    class Meta:
        model = blogmodel
        fields = ['wrtier','title','body' ]


# class ReceiverForm(forms.Form):
#     phone_number = forms.RegexField(regex=r'^(\+98|0)?9\d{9}$',
#                                     error_message=(
#                                         "Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."))
    