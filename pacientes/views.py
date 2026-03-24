from django.shortcuts import render
from .models import Paciente, Propietario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PacienteForm, PropietarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
# R: READ (lista de pacientes)
# SELECT * FROM tabla;
# ==================================
#  *VISTAS RELACIONADAS A PACIENTES
# ==================================
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    context_object_name = 'pacientes'

class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente creado exitosamente."

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente actualizado exitosamente."

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente_list')

    def form_valid(self, form):
        messages.success(self.request, "Paciente eliminado exitosamente.")
        return super().form_valid(form)

# =====================================
#  *VISTAS RELACIONADAS A PROPIETARIOS
# ====================================

class PropietarioListView(LoginRequiredMixin, ListView):
    model = Propietario
    template_name = 'pacientes/propietario_list.html'
    context_object_name = 'propietarios'

class PropietarioCreateView(LoginRequiredMixin, CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'pacientes/propietario_form.html'
    success_url = reverse_lazy('propietario_list')
    success_message = "Propietario creado exitosamente."

class PropietarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'pacientes/propietario_form.html'
    success_url = reverse_lazy('propietario_list')
    success_message = "Propietario actualizado exitosamente."

class PropietarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Propietario
    success_url = reverse_lazy('propietario_list')

    def form_valid(self, form):
        messages.success(self.request, "Propietario eliminado exitosamente.")
        return super().form_valid(form)