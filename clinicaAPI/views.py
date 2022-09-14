from ast import Return
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def index(request):
    return HttpResponse("Hola Mundo")

def consultarPaciente(request):
    if request.method == 'GET':
        return HttpResponse("Aqui se muestra la informacion de un paciente")
    else:
        return HttpResponseNotAllowed(['GET'],"Metodo Invalido")
    

def agregarPersona(request):
    if request.method == 'POST':
        return HttpResponse("Se va a agregar un nuevo miembro")
    else:
        return HttpResponseNotAllowed(['POST'],"Metodo Invalido")


