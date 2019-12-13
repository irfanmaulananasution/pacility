from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TestimonyForm
from .models import Testimony
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

def testimony(request):
        #sendJson
        testimonyJson = serializers.serialize('json', Testimony.objects.all())
        if request.is_ajax():
                return JsonResponse({'testimony' : testimonyJson})
        
        form = TestimonyForm(initial={'username' : request.user.username})
        testimony = Testimony.objects.all()        
        if request.user.is_authenticated:
                return render(request, 'testimonyUser.html', {'form': form, 'testimony': testimony})
        else :
                return render(request, 'testimony.html', {'testimony': testimony})
        
def add_testimony(request):
        if request.user.is_authenticated :
                if request.method == 'POST':
                        form = TestimonyForm(request.POST)
                        if form.is_valid():
                                username = request.user.username
                                title = form.cleaned_data['title']
                                content = form.cleaned_data['content']
                                
                                testimony = Testimony(username = username, title = title, content = content)
                                testimony.save()

        return HttpResponseRedirect(reverse('testimony:testimony'))
