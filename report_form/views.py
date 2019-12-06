from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReportForm
from .models import Report
from datetime import datetime
from report_list.views import report_list
from .urls import *
import logging

def index(request):
    logging.getLogger(__name__).debug("gagaggaa")
    form = ReportForm()
    reports = Report.objects.all()
    return render(request, 'report_form/report_form.html', {'form': form, 'reports': reports})

def add_report(request):
    form = ReportForm()
    reports = Report.objects.all()
    if(request.method == 'POST'):
        logging.getLogger(__name__).debug("gagaggaa")
        form = ReportForm(request.POST)
        # reports = Report.objects.all()
        if form.is_valid():
            
            new_form = form.save(commit=False)
            new_form.save()
            return redirect("report_list:report_list")
    else:
        form = ReportForm()
    return render(request, 'report_form/report_form.html', {'form': form, 'reports' : Report.objects.all()})
