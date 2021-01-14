from django.urls import path

from . import views

app_name='app_medicamentos'
urlpatterns = [
    path( '', views.app_medicamentos, name='medicamentos')
]
