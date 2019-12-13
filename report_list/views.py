from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from report_form.models import Report
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def report_list(request):
	reports = Report.objects.all()
	return render(request, 'report_list/report_list.html', {'reports': reports, 'user':request.user})


