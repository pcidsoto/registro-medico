from django.urls import path
from . import views

app_name = 'app_home'

urlpatterns = [
    path('home/', views.home, name="Home"),
]
