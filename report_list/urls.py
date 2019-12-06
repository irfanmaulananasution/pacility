from django.urls import path
from . import views

app_name='report_list'

urlpatterns = [
	path('', views.report_list, name= 'report_list'),
	#path('', views.add_report, name= 'add_report_form'),
]