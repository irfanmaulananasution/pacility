from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TestimonyForm
from .models import Testimony


def testimony(request):
	form = TestimonyForm()
	testimony = Testimony.objects.all()
	return render(request, 'testimony.html', {'form': form, 'testimony': testimony})

def add_testimony(request):
	if request.method == 'POST':
		form = TestimonyForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			
			testimony = Testimony(username = username, title = title, content = content)
			testimony.save()

	return HttpResponseRedirect(reverse('testimony:testimony'))