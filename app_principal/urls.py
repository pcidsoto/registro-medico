from django.urls import path
from . import views

app_name='app_principal'

urlpatterns = [
    path('', views.principal, name='principal' )
]