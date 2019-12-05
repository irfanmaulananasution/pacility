from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AnnouncementForm
from .models import Announcement
from datetime import datetime, timedelta

def index(request):
	context = {
		"form": AnnouncementForm(),
		"announcements": Announcement.objects.all()
	}

	return render(request, 'homepage/homepage.html', context)