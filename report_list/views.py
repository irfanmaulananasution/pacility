from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from report_form.models import Report

def report_list(request):
	reports = Report.objects.all()
	return render(request, 'report_list/report_list.html', {'reports': reports})


