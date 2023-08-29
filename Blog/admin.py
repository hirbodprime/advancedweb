from django.contrib import admin

# Register your models here.
from .models import blogmodel , contactModel

class blogmodeladmin(admin.ModelAdmin):
    list_display = ['slug' ,'id', 'title']

admin.site.register(blogmodel , blogmodeladmin)
admin.site.register(contactModel)