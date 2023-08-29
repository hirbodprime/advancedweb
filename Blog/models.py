from django.db import models
import os
import random




# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
# def upload_image_path(instance, filename):
#     new_name = random.randint(1, 27634723542)
#     name, ext = get_filename_ext(filename)
#     # final_name = f"{new_name}{ext}"
#     final_name = f"{instance.username}-{ext}-{new_name}"
#     return f"profile/{final_name}"


class blogmodel(models.Model):
    wrtier = models.CharField(max_length=20)
    title = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField(unique=True , null=True , blank=True)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
<<<<<<< HEAD:Blog/models.py
=======
    phone_number = models.CharField(max_length=20, null=True , blank=True)
>>>>>>> e39282af7ba2360966acc8113554803c3bf5ba8c:Drf/models.py
    def __str__(self):
        return self.title 

class contactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    slug = models.SlugField(unique=True , null=True , blank=True)
    body=models.TextField(max_length=1500)
    status =models.BooleanField(null=True,blank=True)
    def __str__(self):
        return self.name 

    