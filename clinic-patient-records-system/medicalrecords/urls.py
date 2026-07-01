from django.urls import path
from . import views

app_name = 'medicalrecords'

urlpatterns = [
    path('', views.home, name='home'),
]
