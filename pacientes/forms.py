from django import forms
from .models import Paciente, Propietario

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'propietario']
        # Widgets sirven para agregar clases css a los campos del formulario, lo que facilita su estilización en el frontend.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), #* <input type="text" class="form-control">
            'especie': forms.Select(attrs={'class': 'form-control'}),#* <select class="form-control">...</select>
            'raza': forms.TextInput(attrs={'class': 'form-control'}),#* <input type="text" class="form-control">
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),#* <input type="date" class="form-control">
            'propietario': forms.Select(attrs={'class': 'form-control'}),#* <select class="form-control">...</select>
        }

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'telefono_contacto', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), #* <input type="email" class="form-control">
        }