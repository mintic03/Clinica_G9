
from django.shortcuts import render
import json
from urllib import response
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Persona, Paciente, SignosVitale, Medico, Familiar, EnfermeroAux

def newPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data["id"], 
                nombre = data["nombre"], 
                apellido = data["apellido"], 
                telefono = data["telefono"], 
                #genero = data["genero"] 
            )
            persona.save()
            return HttpResponse("Persona Agregada")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def newPacien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["userId"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe persona con ese ID")
            paciente = Paciente(
                persona = pers, 
                direccion = data["direccion"], 
                ciudad = data["ciudad"], 
                fechaNto = data["fechaNto"],
                latitud = data["latitud"],
                longitud = data["longitud"], 
                
            )
            paciente.save()
            return HttpResponse("Paciente Agregada")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")
            
          

def newSignoVital(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe paciente con ID")

            signovital = SignosVitale( 
                paciente = paciente, 
                tipo = data["tipo"],
                valor = data["valor"], 
                fecha = data["fecha"],
            )
            signovital.save()
            return HttpResponse("Signos Agregados")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")


def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con ID")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe paciente con ID")
            signos = SignosVitale.objects.filter(id = data["signosId"]).first()
            if (not signos):
                return HttpResponseBadRequest("No existe registro de signos")
            
            medico = Medico( 
                paciente = paciente, 
                persona = persona,
                signos = signos,
                especialidad = data["especialidad"],
            )
            medico.save()
            return HttpResponse("Signos Agregados")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def newFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con ID")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe paciente con ID")

            familiar = Familiar(
                persona = persona, 
                paciente = paciente, 
                #parentesco = parentesco, 
                email = data["email"],
            )
            familiar.save()
            return HttpResponse("Familiar Agregado")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def newEnfermero(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con ID")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe paciente con ID")
            signos = SignosVitale.objects.filter(id = data["signosId"]).first()
            if (not signos):
                return HttpResponseBadRequest("No existe registro de signos")
            
            enfermero = EnfermeroAux( 
                paciente = paciente, 
                persona = persona,
                signos = signos,
                
            )
            enfermero.save()
            return HttpResponse("Signos Agregados")
        except:
            return HttpResponseBadRequest("Error en los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def getAllPacientes(request):
    if request.method == 'GET':
        pacientes=Paciente.objects.all()
        if (not pacientes):
            return HttpResponseBadRequest("No hay pacientes en la BD")

        personas=Persona.objects.all()
        if(not personas):
            return HttpResponseBadRequest("No hay personas en la BD")

        allPacienteDta=[]
        for x,y in zip(pacientes,personas):
            data={
                "id":x.id,
                "nombre":y.nombre,
                "apellido":y.apellido,
                "telefono":y.telefono,
                "genero":y.genero,
                "direccion":x.direccion,
                "ciudad":x.ciudad,
                "fechaNto":x.fechaNto,
                "latitud":x.latitud,
                "longitud":x.longitud
            }
            allPacienteDta.append(data)
        dataJson = json.dumps(allPacienteDta)
        resp=HttpResponse()
        resp.headers['Content-Type']="text/json"
        resp.content=dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Metodo Invalido")

def getOnePaciente(request,id):
    if request.method == 'GET':
        paciente=Paciente.objects.filter(id=id).first()
        if (not paciente):
            return HttpResponseBadRequest("No hay paciente con ese ID")

        persona=Persona.objects.filter(paciente=id).first()
        if(not persona):
            return HttpResponseBadRequest("No hay persona con ese ID")

        Dta={
            "id":paciente.id,
            "nombre":persona.nombre,
            "apellido":persona.apellido,
            "telefono":persona.telefono,
            "genero":persona.genero,
            "direccion":paciente.direccion,
            "ciudad":paciente.ciudad,
            "fechaNto":paciente.fechaNto,
            "latitud":paciente.latitud,
            "longitud":paciente.longitud
        }               
        dataJson = json.dumps(Dta)
        resp=HttpResponse()
        resp.headers['Content-Type']="text/json"
        resp.content=dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Metodo Invalido")

