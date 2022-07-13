from django.urls import path
from .views import CustomUserView
urlpatterns = [
    path("sign-in/" ,CustomUserView.as_view(),name="signin" )
]