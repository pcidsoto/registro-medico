# Create your views here.

import json
from django.shortcuts import render
from django.conf import settings
from . forms import Pacientes

# Create your views here.
filename = '/data/data_registros.json'

def get_examenes(filename, settings, run):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    datos_examenes = {}
    for elemento in pacientes['pacientes']:
        for clave in elemento.keys():
            if clave == run:
                datos_examenes['run'] = clave
                datos_examenes.update(elemento[clave]['datos_personales'])
                datos_examenes.update(elemento[clave]['examenes'])
    return datos_examenes

def grafico_hemograma(data):
    fechas_hemograma = []
    hematocrito = []
    hemoglobina = []
    datos= {}
    for elemento in data['Hemograma']:
        for clave,valor  in elemento.items():
            #fecha = datetime.datetime.strptime(clave, '%d-%m-%Y')
            #fechas_hemograma.append([fecha,0])
            fechas_hemograma.append(clave)
            hematocrito.append(valor['Hematocrito'])
            hemoglobina.append(valor['Hemoglobina'])
    datos['fechas'] = fechas_hemograma
    datos['Hematocrito'] = hematocrito
    datos['Hemoglobina'] = hemoglobina
    print(datos['fechas'])
    return datos

def grafico_plipidico(data):
    fechas_plipidico = []
    colesterol = []
    bilirrubina = []
    datos= {}
    for elemento in data['perfil_lipidico']:
        for clave,valor  in elemento.items():
            #fecha = datetime.datetime.strptime(clave, '%d-%m-%Y')
            #fechas_hemograma.append([fecha,0])
            fechas_plipidico.append(clave)
            colesterol.append(valor['Colesterol'])
            bilirrubina.append(valor['Bilirrubina'])
    datos['fechas'] = fechas_plipidico
    datos['colesterol'] = colesterol
    datos['bilirrubina'] = bilirrubina
    print(datos['fechas'])
    return datos

def grafico_pbioquimico(data):
    fechas_pbioquimico = []
    ptd = []
    tbr = []
    datos= {}
    for elemento in data['perfil_bioquimico']:
        for clave,valor in elemento.items():
            #fecha = datetime.datetime.strptime(clave, '%d-%m-%Y')
            #fechas_hemograma.append([fecha,0])
            fechas_pbioquimico.append(clave)
            ptd.append(valor['PTD'])
            tbr.append(valor['TBR'])
    datos['fechas'] = fechas_pbioquimico
    datos['PTD'] = ptd
    datos['TBR'] = tbr
    print(datos['fechas'])
    return datos

def grafico_parterial(data):
    fechas_parterial = []
    fm = []
    fn = []
    datos= {}
    for elemento in data['presion_arterial']:
        for clave,valor  in elemento.items():
            #fecha = datetime.datetime.strptime(clave, '%d-%m-%Y')
            #fechas_hemograma.append([fecha,0])
            fechas_parterial.append(clave)
            fm.append(valor['F_manana'])
            fn.append(valor['F_tarde'])
    datos['fechas'] = fechas_parterial
    datos['F_manana'] = fm
    datos['F_tarde'] = fn
    print(datos['fechas'])
    return datos

def examenes(request):
    

    if request.method == 'POST':
        seleccionar = Pacientes()
        rut = request.POST['pacientes'] 
        datos = get_examenes(filename, settings, rut)
        hemograma = grafico_hemograma(datos)
        plipidico = grafico_plipidico(datos)
        pbioquimico = grafico_pbioquimico(datos)
        parterial = grafico_parterial(datos)
        context = {"nombre": datos["nombre"], 
                "apellido": datos["apellido"],
                "edad": datos["edad"],
                "hemograma": datos["Hemograma"],
                "perfil_lipidico": datos["perfil_lipidico"],
                "presion_arterial": datos["presion_arterial"],
                "perfil_bioquimico": datos["perfil_bioquimico"],
                "hemograma_grafico":hemograma,
                "plipidico_grafico":plipidico,
                "pbioquimico_grafico":pbioquimico,
                "parterial_grafico":parterial,
                "seleccionar":seleccionar}
        return render(request, 'app_examenes/examenes.html', context)
    else:
        seleccionar = Pacientes()
        context = {'seleccionar': seleccionar}
        return render(request, 'app_examenes/examenes.html', context)

