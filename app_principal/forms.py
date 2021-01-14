from django import forms

class LoginForm(forms.Form):

    user = forms.CharField(
        label = 'Usuario',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '99.999.999-9',
        })
    )

    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Ingrese su contraseña'
        })
    )