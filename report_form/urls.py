from django.urls import path
from . import views

app_name = 'report_form'

urlpatterns = [
	path('', views.add_report, name= 'report_form'),
	path('report_service/', views.add_report_service, name= 'add_report_service'),

]
