from django.shortcuts import render
from .forms import  FormUser
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import CustomUsers



class CustomUserView(CreateView):
    model = CustomUsers
    template_name = "user/signin.html"
    fields = ['username', 'email' ,'phone_number', 'first_name','last_name' , 'profile_image', 'password','re_password']
    def get_success_url(self):
        from django.urls import reverse
        return reverse("ListViewPostallNAME")

