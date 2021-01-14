from django.urls import path
from . import views

app_name = 'app_examenes'

urlpatterns = [
    path('', views.examenes, name='examen'),


]
