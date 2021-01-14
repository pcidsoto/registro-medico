from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
import datetime

def validar_fecha(fecha):
    fecha_base = datetime.datetime.strptime("01-01-1920", "%d-%m-%Y").date()
    if fecha >= fecha_base:
        return fecha
    else:
        raise ValidationError("Sólo fechas mayores o iguales a 1920")

class RegistroPaciente(forms.Form):

    run = forms.CharField(
        label='R.U.N',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'9.999.999-9'},
            ),
        validators=[validators.MaxLengthValidator(12,'Rut Incorrecto!'),
                validators.MinLengthValidator(11,'Rut Incorrecto')]
        )
    nombre = forms.CharField(
        label='Nombre',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su nombre'})
        )
    apellido = forms.CharField(
        label='Apellido',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su apellido'})
        )
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget= forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder':'Año-Mes-Dia'}
            ),
        validators=[validar_fecha]
        )



class LoginForm(forms.Form):

    user = forms.CharField(
        label = 'Usuario',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Usuario'
        })
    )

    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su contraseña'
        })
    )