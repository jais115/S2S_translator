# from django.shortcuts import render
# from gtts import gTTS
# from django.template import Context
# # Importing necessary modules required
# from playsound import playsound
# import speech_recognition as sr 
# import pyttsx3
# from googletrans import Translator
# from gtts import gTTS
# import os
# import time
# from pydub import AudioSegment
# from pydub.playback import play
# from queue import Queue
# import threading
# from say import *
# import gtts

# # Create your views here.
# from django.shortcuts import render, redirect
# #pytub package for download youtube video
# from pytube import YouTube
# import os
# from django.http import FileResponse
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.conf import settings as django_settings
# import os
# import wave
# import speech_recognition as sr
# import pyttsx3
# from django.core.files.storage import default_storage
# from .models import *
# import speech_recognition as spr
# from googletrans import Translator
# from urllib import parse
# import requests as requests
# import re
# import base64

# r = sr.Recognizer()

# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
#     # return JsonResponse({'success':False, 'errorMsg':errorMsg})


# def TTSHome(request):
#     if is_ajax(request):
#     # python3

#     #if request.is_ajax():
#         print('a===>>>>>', request.GET.get('datas'))
#         print('a===>>>>>', request.FILES.get('datas'))
#         print('a===>>>>>', request.GET.get('datas'))


#     if request.method == 'POST':
#         file = request.FILES.get('file')
#         lang = request.POST.get('lang')
#         dlang = request.POST.get('dlang')
#         aobj = AudioModel()
#         aobj.audioname = 'temp1'
#         aobj.audio = file
#         aobj.save()
#         # Using ggogle to recognize audio
#         audio = AudioModel.objects.last()
#         adurl = str(audio.audio.url)
#         with sr.WavFile(adurl[1:]) as source:
#             audio = r.record(source)
#             text = r.recognize_google(audio, language=dlang)
#         translator = Translator()
#         ttext = translator.translate(text, src=dlang, dest=lang)
#         # text1 =  ttext.text
#         # say = gtts.gTTS(text=text1, lang=lang, slow=False)

#         coded_string = request.POST.get('blobdata') 

#         sample_string_bytes = coded_string.encode("UTF-8")
#         imgdata = base64.b64decode(sample_string_bytes)
#         filename = 'some_image.wav'  # I assume you have a way of picking unique filenames
#         with open(filename, 'wb') as f:
#             f.write(imgdata)

#         context = {
#             'text': ttext,
#             'lang': lang,
#         }
#         return render(request, 'transcript/ttshome.html', context)

#     context = {

#     }
#     return render(request, 'transcript/ttshome.html', context)

from django.shortcuts import render, redirect
#pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings as django_settings
import os
import wave
import speech_recognition as sr
import pyttsx3
from django.core.files.storage import default_storage
from .models import *
import speech_recognition as spr
from googletrans import Translator
from urllib import parse
import requests as requests
import re
import base64
r = sr.Recognizer()

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def TTSHome(request):
    if is_ajax(request):
    # python3

    #if request.is_ajax():
        print('a===>>>>>', request.GET.get('datas'))
        print('a===>>>>>', request.FILES.get('datas'))
        print('a===>>>>>', request.GET.get('datas'))


    if request.method == 'POST':
        file = request.FILES.get('file')
        lang = request.POST.get('lang')
        dlang = request.POST.get('dlang')
        aobj = AudioModel()
        aobj.audioname = 'temp1'
        aobj.audio = file
        aobj.save()
        # Using ggogle to recognize audio
        audio = AudioModel.objects.last()
        adurl = str(audio.audio.url)
        with spr.WavFile(adurl[1:]) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language=dlang)
        translator = Translator()
        ttext = translator.translate(text, src=dlang, dest=lang)

        coded_string = request.POST.get('blobdata')

        sample_string_bytes = coded_string.encode("UTF-8")
        imgdata = base64.b64decode(sample_string_bytes)
        filename = 'some_image.wav'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        context = {
            'text': ttext,
            'lang': lang,
        }
        return render(request, 'index.html', context)

    context = {

    }
    return render(request, 'index.html', context)