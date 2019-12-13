from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
	path('', views.index, name='index'),
	path('add_announcement', views.add_announcement, name='add_announcement'),
	path('get_announcements', views.get_announcements, name='get_announcements'),
]