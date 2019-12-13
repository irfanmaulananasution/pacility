from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AnnouncementForm
from .models import Announcement
from datetime import datetime, timedelta
from django.http.response import JsonResponse

def index(request):
	context = {
		"form": AnnouncementForm(),
		"announcements": Announcement.objects.all()
	}

	return render(request, 'homepage/homepage.html', context)

def add_announcement(request):
	if request.method == 'POST':
		form = AnnouncementForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			initial = username[:1].upper()
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']

			now = datetime.now() + timedelta(hours=7)
			day = now.strftime("%A")
			date = now.strftime("%e")
			month = now.strftime("%B")
			year = now.strftime("%Y")
			hour = now.strftime("%H")
			minute = now.strftime("%M")
			fulldate = f"{day}, {date} {month} {year}"
			time = f"{hour}:{minute} WIB"

			announcement = Announcement(username = username, initial = initial, title = title, content = content, date = fulldate, time = time)
			announcement.save()

	return HttpResponseRedirect(reverse('homepage:index'))

def get_announcements(request):
	announcements = Announcement.objects.all().values()
	announcement_dict = {'announcements': list(announcements)}
	return JsonResponse(announcement_dict, safe=False)