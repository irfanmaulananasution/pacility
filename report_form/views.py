from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReportForm
from .models import Report
from datetime import datetime

def index(request):
	form = ReportForm()
	reports = Report.objects.all()
	return render(request, 'report_form/report_form.html', {'form': form, 'reports': reports})

def add_report(request):
    if(request.method == 'POST'):
        form = ReportForm(request.POST)
        if form.is_valid():
            form_title = form.changed_data['form_title']
            location = form.changed_data['location']
            time = form.changed_data['time']
            category = form.changed_data['category']
            description =  form.changed_data['description']

            report = Report(
                form_title = form_title,
                location = location,
                time = time,
                category = category,
                description = description
            )
            report.save()

    return HttpResponseRedirect(reverse('report_form:index'))