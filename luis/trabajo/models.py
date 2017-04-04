from django.db import models
from django.core.urlresolvers import reverse



class Estudiante(models.Model):
	"""docstring for ClassName"""
	nombres=models.CharField(max_length=110,blank=True)
	apellidos=models.CharField(max_length=110,blank=True)
	direccion=models.CharField(max_length=110,blank=True)
	edad=models.CharField(max_length=110,blank=True)
	correo=models.EmailField(max_length=50)
	def __str__(self):
		return self.nombres+" "+self.apellidos
        
class Materia(models.Model):
	"""docstring for ClassName"""
	nombre=models.CharField(max_length=110,blank=True)
	profesor=models.CharField(max_length=110,blank=True)
	identificacion=models.CharField(max_length=110,blank=True)
	def __str__(self):
		return self.nombre+" "+self.profesor
