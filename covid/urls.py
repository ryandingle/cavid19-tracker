from django.urls import path
from . import views

app_name = 'covid'
urlpatterns = [
	path('', views.V1.as_view()),
	path('download', views.V2.as_view(), name='download'),
]