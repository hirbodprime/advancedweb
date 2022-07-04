from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("advapp.urls")),
    path('drf/' , include("Drf.urls")),
    path('profile/',include("fullprofile.urls"))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
