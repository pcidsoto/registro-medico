from django import forms
from django.conf import settings
import json

filename = '/data/data_registros.json'
def get_pacientes(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    lista_pacientes=[['--', '--']]

    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            lista_pacientes.append((clave,clave))
            
    return lista_pacientes

pacientes = get_pacientes(filename, settings)

class Pacientes(forms.Form):
    pacientes = forms.CharField(
        label = False,
        widget = forms.Select(choices = pacientes, attrs={'class':'form-select'})
    )
