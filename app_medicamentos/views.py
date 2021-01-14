import json
from django.shortcuts import render
from django.conf import settings
from . forms import Pacientes

# Create your views here.
filename = '/data/data_registros.json'

def get_medicamentos(filename, settings, run):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    datos_medicamentos = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            if clave == run:
                datos_medicamentos['run'] = clave
                datos_medicamentos.update(elemento[clave]['datos_personales'])
                datos_medicamentos.update(elemento[clave]['medicamentos'])
    
    return datos_medicamentos

def app_medicamentos(request):
    if request.POST:
        run = request.POST['pacientes'] 
        datos_medicamentos = get_medicamentos(filename, settings, run)
                
        seleccionar = Pacientes()
        context = {'seleccionar':seleccionar, 'nombre':datos_medicamentos['nombre'],
                'apellido':datos_medicamentos['apellido'], 'recetas':datos_medicamentos['recetas']
                }
        return render(request, 'app_medicamentos/medicamento.html', context)
    else:
        seleccionar = Pacientes()
        context = {'seleccionar':seleccionar}
        return render(request, 'app_medicamentos/medicamento.html', context)




 
