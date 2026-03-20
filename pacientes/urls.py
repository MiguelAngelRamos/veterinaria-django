from django.urls import path
from . import views

urlpatterns = [
    # Rutas Pacientes
    path('', views.PacienteListView.as_view(), name='paciente_list'),
    path('nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('eliminar/<int:pk>/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
    # Rutas Propietarios
    path('propietarios/', views.PropietarioListView.as_view(), name='propietario_list'),
    path('propietarios/nuevo/', views.PropietarioCreateView.as_view(), name='propietario_create'),
]
# http://127.0.0.1:8000/