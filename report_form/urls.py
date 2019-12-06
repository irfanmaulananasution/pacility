from django.urls import path
from . import views

app_name = 'report_form'

urlpatterns = [
	path('', views.index, name= 'report_form'),
	path('', views.add_report, name= 'add_report'),
]
