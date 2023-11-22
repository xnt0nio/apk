from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('descargar-apk/', download_apk, name='download_apk'),

  
]