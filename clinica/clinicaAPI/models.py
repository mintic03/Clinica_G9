from operator import mod
from tkinter import CASCADE
from django.db import models

class Registro(models.Model):
    id = models.BigIntegerField(primary_key = True)
    contrase = models.IntegerField()

class Persona(models.Model):
    id = models.BigIntegerField(primary_key = True)
    nombre = models.CharField(max_length = 45)
    apellido = models.CharField(max_length = 45)
    telefono = models.BigIntegerField()
    genero = [
		('F','Femenino'),
		('M','Masculino')
	]
    genero = models.CharField(max_length = 1, choices = genero, default ='F') 

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, default=1, on_delete=models.CASCADE)
    direccion = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 45)
    fecha_Nacimiento = models.CharField(max_length=15)
    latitud = models.FloatField()
    longitud = models.FloatField()

class SignosVitale(models.Model):
    id =models.AutoField(primary_key=True)
    paciente= models.ForeignKey(Paciente, on_delete = models.CASCADE)
    tipo_signo_vital = models.CharField(max_length = 70)
    valor_signo_vital = models.CharField(max_length = 45)
    fecha = models.CharField(max_length=15)

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, default=1, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length = 45)
    signos=models.ForeignKey(SignosVitale, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


class EnfermeroAux(models.Model):
    id= models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, default=1, on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE)
    signos=models.ForeignKey(SignosVitale, on_delete=models.CASCADE)

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    persona= models.ForeignKey(Persona, on_delete = models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=30)
    e_mail = models.EmailField()
    