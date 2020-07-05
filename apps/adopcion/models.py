from django.db import models


class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)
		

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,null=True,blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

	def __str__(self):
		texto = 'Solicitante {} {} sus razones son: {}'
		return texto.format(self.persona.nombre, self.persona.apellido, self.razones)
