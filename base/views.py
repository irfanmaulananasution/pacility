from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse('Success')
		return HttpResponse('Not Found')

	return HttpResponseRedirect(reverse('homepage:index'))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage:index'))

def register(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
		new_user.save()

		user = authenticate(request, username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('homepage:index'))

	return HttpResponseRedirect(reverse('homepage:index'))