
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Consumir

def listar_alumnos(request):

    test = "test"
    alumnos_response = requests.get("http://127.0.0.1:8000/api/alumnos/")
    # print("CONTEXT: ", alumnos_response.content)
    # print("TEXT: ", alumnos_response.text)
    # print("JSON: ", alumnos_response.json)

    data = alumnos_response.json()
    print(data[0]['id'])

    for alumno in data:
        id = alumno['id']
        nombre = alumno["nombre"]
        apellido = alumno['apellido']
        edad = alumno['edad']
        carrera = alumno['carrera']
        matricula = alumno['matricula']

        context = {
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "carrera": carrera,
            "matricula": matricula,
        }


    return render(request, 'alumnos/alumnos_list.html', {"test": test, "context": context})

def detalles_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def crear_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def editar_alumnos(request):
    return (request, 'lista.html', {"test": "test"})

def eliminar_alumnos(request):
    return (request, 'lista.html', {"test": "test"})
