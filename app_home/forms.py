from django import forms
from django.conf import settings
import json

filename = '/data/data_registros.json'

def leer_pacientes(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    print(pacientes)
    lista_pacientes= [('-------','--------')]
    
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():

            lista_pacientes.append((clave,clave))
    return lista_pacientes

users = leer_pacientes(filename, settings)
class Pacientes(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = users, attrs={'class':'form-select'})
    )

