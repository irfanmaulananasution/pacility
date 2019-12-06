from django.urls import path
from . import views

app_name = 'testimony'

urlpatterns = [
	path('', views.testimony, name='testimony'),
	path('add_testimony/', views.add_testimony, name="add_testimony"),
]