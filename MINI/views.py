from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from . import settings
from steganogan import SteganoGAN
import string
import random

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        steganogan = SteganoGAN.load(architecture='dense')
        # print(request.body)
        # s = request.body.decode('utf')
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))
        res=res+'.png'
        # print(res)
        f = request.FILES['file']
        path = default_storage.save(res, ContentFile(f.read()))
        
        # print(s)
        steganogan.encode(settings.MEDIA_ROOT + '/' + res, settings.MEDIA_ROOT + '/output/' + res, 'This is a super secret message!')
        return redirect(settings.MEDIA_URL + res)