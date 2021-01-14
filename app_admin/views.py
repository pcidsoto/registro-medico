from django.shortcuts import render, redirect
from .forms import RegistroPaciente, LoginForm
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

filename = '/data/data_registros.json'


def login(request):
    login = LoginForm()
    if request.method == 'POST':    
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            if data['user'] == 'user' and data['password'] == 'pass':

                return redirect('app_admin:registro')
            else:
                return redirect('app_admin:login')
        else:
            return render(request, 'app_admin/login.html',context)
    else:
        context = {'login_form': login}
        return render(request, 'app_admin/login.html', context)










#lee todo el archivo y devuelve un diccionario
def leer_archivo(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    return pacientes

# guarda los datos modificados como diccionario en el archivo.
# nota: primero leer el archivo para modificarlo
# la funcion sobreescribe todo el archivo
def actualizar_archivo(filename, data, settings):
    with open(str(settings.BASE_DIR)+filename, 'w') as file:
        json.dump(data, file)

# traigo solo la información que necesito mostrar
# y retorno un diccionario
def leer_pacientes(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)

    lista_pacientes= []
    
    for elemento in pacientes['pacientes']:
        for clave, value in elemento.items(): 
            datos = {}
            datos['run'] = clave
            datos.update(elemento[clave]['datos_personales'])
            datos.update(elemento[clave]['datos_personales'])
            lista_pacientes.append(datos)
    return lista_pacientes

# agrega un paciente al archivo seteando todo el diccionario de
# datos.
def agregar_paciente(filename, form_data, settings):
    form_data['fecha_nacimiento']=form_data['fecha_nacimiento'].strftime("%d-%m-%Y")

    run = form_data['run']
    datos_personales = {}
    datos_personales['nombre'] = form_data['nombre']
    datos_personales['apellido'] = form_data['apellido']
    datos_personales['edad'] = ''
    datos_personales['f_nacimiento'] = form_data['fecha_nacimiento']

    data ={}
    data[run] = {}
    data[run]['datos_personales'] = datos_personales
    data[run]['datos_contacto'] = {}
    data[run]['password'] = "12345"
    data[run]['examenes'] = {}
    data[run]['examenes']['Hemograma'] = []
    data[run]['examenes']['perfil_lipidico'] = []
    data[run]['examenes']['perfil_bioquimico'] = []
    data[run]['examenes']['presion_arterial'] = []
    data[run]['medicamentos'] = {}
    data[run]['medicamentos']['recetas'] = []
    

    archivo = leer_archivo(filename, settings)
    archivo['pacientes'].append(data)

    actualizar_archivo(filename, archivo, settings)
    

def registro(request):
    if request.method == 'POST':
        data_post = RegistroPaciente(request.POST)
        if data_post.is_valid():
            data_post = data_post.cleaned_data
            agregar_paciente(filename, data_post, settings)

            pacientes = leer_pacientes(filename, settings)
            page = request.GET.get('page', 1)

            paginator = Paginator(pacientes, 5)
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            formulario = RegistroPaciente()
            context = {'form': formulario, 'registros': users }
            print("PACIENTE AGREGADO")
            return render(request, 'app_admin/registro.html', context=context)
        else:
            print('NO ES VALIDO')
            pacientes = leer_pacientes(filename, settings)
            page = request.GET.get('page', 1)

            paginator = Paginator(pacientes, 5)
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            context = {'form': data_post, 'registros': users }
            return render(request, 'app_admin/registro.html', context)
    else:
        pacientes = leer_pacientes(filename, settings)
        page = request.GET.get('page', 1)

        paginator = Paginator(pacientes, 5)
        try:
            registros = paginator.page(page)
        except PageNotAnInteger:
            registros = paginator.page(1)
        except EmptyPage:
            registros = paginator.page(paginator.num_pages)

        print("CREANDO FORMULARIO")
        formulario = RegistroPaciente()
        context = {'form': formulario, 'registros': registros }
        return render(request, 'app_admin/registro.html', context=context)


def eliminar(request, run):
    print('ELIMINANDO -> {}'.format(run))
    pacientes = leer_archivo(filename, settings)
    for i, elemento in enumerate(pacientes['pacientes']):
        for clave, valor in elemento.items():
            if clave == run:
                pacientes['pacientes'].pop(i)

    actualizar_archivo(filename, pacientes, settings)
    
    return redirect('app_admin:registro')
