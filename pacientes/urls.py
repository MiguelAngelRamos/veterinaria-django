from django.urls import path
from . import views

urlpatterns = [
        # Ruta Registro
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    # Rutas Pacientes
    path('', views.PacienteListView.as_view(), name='paciente_list'),
    path('nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('eliminar/<int:pk>/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
    # Rutas Propietarios
    path('propietarios/', views.PropietarioListView.as_view(), name='propietario_list'),
    path('propietarios/nuevo/', views.PropietarioCreateView.as_view(), name='propietario_create'),
    path('propietarios/editar/<int:pk>/', views.PropietarioUpdateView.as_view(), name='propietario_update'),
    path('propietarios/eliminar/<int:pk>/', views.PropietarioDeleteView.as_view(), name='propietario_delete'),
]
# http://127.0.0.1:8000/propietarios/editar/1/ -> editamos a Sofia, la propietaria de Rocky