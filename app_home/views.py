from django.shortcuts import render
from .forms import Pacientes
from django.conf import settings
import json

filename = '/data/data_registros.json'

def get_paciente(filename, run ,settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)

    datos = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys(): 
            if clave == run:
                datos['run'] = clave
                datos.update(elemento[clave]['datos_personales'])
                datos.update(elemento[clave]['datos_contacto'])
                
    return datos


# Create your views here.
def home(request):
    if request.POST: 
        run = request.POST['pacientes'] 
        datos_paciente = get_paciente(filename, run, settings)
        print(datos_paciente)
        pacientes = Pacientes(auto_id=False)
        context = {'pacientes':pacientes, 'datos': datos_paciente}
        return render(request, 'app_home/home.html', context)

    else:
        pacientes = Pacientes(auto_id=False)
        context = {'pacientes':pacientes }
        return render(request, 'app_home/home.html', context)

