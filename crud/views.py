from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer

from rest_framework.decorators import api_view

@api_view(['GET'])
def api_alumno_listar(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_alumno_detalles(request, id):
    alumnos = Alumno.objects.get(id=id)
    serializer = AlumnoSerializer(alumnos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def api_alumno_crear(request):
    serializer = AlumnoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def api_alumno_editar(request, id):
    alumno = Alumno.objects.get(id=id)
    serializer = AlumnoSerializer(instance=alumno, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def api_alumno_eliminar(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    return Response('Delete')


# Consumir

def listar_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def detalles_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def crear_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def editar_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def eliminar_alumnos(request):
    return (request, 'lista.html', {"test": "test"})




