from django.urls import path

from .import views

urlpatterns = [
    path('', views.api_alumno_listar, name='api_lista_alumnos'),
    path('detalles/<str:id>/', views.api_alumno_detalles, name="api_alumno_detalles"),
    path('crear', views.api_alumno_crear, name="api_alumno_crear"),
    path('editar/<str:id>/', views.api_alumno_editar, name="api_alumno_editar"),
    path('eliminar/<str:id>/', views.api_alumno_eliminar, name="api_alumno_eliminar"),
]
