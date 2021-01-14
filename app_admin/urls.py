from django.urls import path
from . import views

app_name = 'app_admin'

urlpatterns = [
    path('registro/', views.registro, name='registro' ),
    path('', views.login, name='login' ),
    path('eliminar/<run>/', views.eliminar, name='eliminar' ),

]
