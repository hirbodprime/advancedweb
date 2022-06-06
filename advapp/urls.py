from turtle import down
from django.urls import path
from .views import download_file , download

urlpatterns = [
    path('' , download , name="downloadpagename"),
    path('download/<filename>' , download_file , name="downloadviewname")
]
