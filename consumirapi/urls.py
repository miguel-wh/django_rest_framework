from django.urls import path

from .import views

urlpatterns = [
    path('', views.listar_alumnos, name='view_lista_alumnos'),
    path('detalles/<str:id>/', views.detalles_alumnos, name="view_alumno_detalles"),
    path('crear', views.crear_alumnos, name="view_alumno_crear"),
    path('editar/<str:id>/', views.editar_alumnos, name="view_alumno_editar"),
    path('eliminar/<str:id>/', views.eliminar_alumnos, name="view_alumno_eliminar"),
]
