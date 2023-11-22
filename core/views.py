from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os


# Create your views here.


from .models import *



def index(request):
    return render(request, 'core/index.html')




def download_apk(request):
    apk_path = os.path.join(settings.MEDIA_ROOT, 'app.apk')  # Ajusta la ruta según tu configuración

    with open(apk_path, 'rb') as apk_file:
        response = HttpResponse(apk_file.read(), content_type='application/vnd.android.package-archive')
        response['Content-Disposition'] = 'attachment; filename="app.apk"'
        return response
