from django.db import models

# Create your models here.
class Persona(models.Model): #Primer Tabla Personas
	id = models.CharField(max_length = 20, primary_key = True)
	Nombre_Enf = models.CharField(max_length = 45)
	Apellido_Enf = models.CharField(max_length = 45)
	Telefono_Enf = models.CharField(max_length = 45)
	Genero = [
		('F','Femenino'),
		('M','Masculino')
	]
	Genero = models.CharField(max_length = 1, choices = Genero, default ='F')

	def nombrecompleto(self): # Funcion para Nombre
		txt="{0}, {1} {2}"
		return txt.format(self.id, self.Nombre_Enf, self.Apellido_Enf)

	def __str__(self):
		txt="{0}"
		return txt.format(self.nombrecompleto())

class Medico(models.Model):
	id_medico = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
	Especialidad = models.CharField(max_length = 50)
	Registro = models.CharField(max_length = 45)

	def nombrecompleto_M(self): # Funcion para Nombre
		txt="{0}, Especialidad: {1}"
		return txt.format(self.id_medico.nombrecompleto(), self.Especialidad)

	def __str__(self):
		txt="Medico: {0}"
		return txt.format(self.nombrecompleto_M())


class Enfermero(models.Model):
	id_enfermero = models.ForeignKey(Persona, null = False, blank = False, on_delete = models.CASCADE)

	def __str__(self):
		txt="Enfermero: {0}"
		return txt.format(self.id_enfermero.nombrecompleto())

class Paciente(models.Model):
	id_paciente = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
	Direccion = models.CharField(max_length = 50)
	Ciudad = models.CharField(max_length = 45)
	Fecha_Nacimiento = models.DateField()
	Latitud = models.CharField(max_length = 50)
	Longitud = models.CharField(max_length = 50)
	Medicos_id = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)

	def nombrecompleto_P(self): # Funcion para Nombre
		txt="{0} "
		return txt.format(self.id_paciente.nombrecompleto())

	def __str__(self):
		txt="Paciente: {0} / Medico: {1}"
		return txt.format(self.nombrecompleto_P(), self.Medicos_id.nombrecompleto_M())

class Familiar(models.Model):
	id_familiar = models.ForeignKey(Persona, null = False, blank = False, on_delete = models.CASCADE)
	Parentesco = [
		('F','Padre/Madre'),
		('S','Hijo/Hija'),
		('B','Hermano/Hermana'),
		('G','Abuelo/Abuela'),
		('O','Otro')
	]
	Parentesco = models.CharField(max_length = 1, choices = Parentesco, default ='F')
	E_mail = models.CharField(max_length = 45)
	Paciente_id = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		txt = "Familiar: {0} / Paciente: {1}"
		return txt.format(self.id_familiar.nombrecompleto(), self.Paciente_id.nombrecompleto_P())

class Signos_vitale(models.Model):
	id_paciente = models.ForeignKey(Paciente, null = False, blank = False, on_delete = models.CASCADE)
	Tipo_signo_vital = models.CharField(max_length = 70)
	Valor_signo_vital = models.CharField(max_length = 45)
	Fecha = models.DateField()

	def __str__(self):
		txt = "Signos vitales: {0}"
		return txt.format(self.id_paciente.nombrecompleto_P())
