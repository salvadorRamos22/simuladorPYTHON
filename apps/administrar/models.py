from django.db import models

class tipoUsuario(models.Model):
	descripcion = models.CharField(max_length=50)
	estado = models.IntegerField()
	def __str__(self):
		return self.descripcion

class usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	password = models.CharField(max_length=256)
	fechaNacimiento = models.DateField()
	sexo = models.CharField(max_length=9)
	email = models.CharField(max_length=250)
	tipoU = models.ForeignKey(tipoUsuario)
	estado = models.IntegerField()
	def __str__(self):
		return self.email

class siembra(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion=models.CharField(max_length=100)
	estado = models.IntegerField()
	def __str__(self):
		return self.nombre

class faseCultivo(models.Model):
	etapa = models.IntegerField()
	descripcion = models.CharField(max_length=50)
	diasDuracion = models.IntegerField()
	hidricos = models.DecimalField(max_digits=5,decimal_places=2)
	siembra = models.IntegerField()
	estado = models.IntegerField()
	def __str__(self):
		return self.descripcion

class configuracion(models.Model):
	temperaturaMax = models.DecimalField(max_digits=5,decimal_places=2)
	temperaturaMin = models.DecimalField(max_digits=5,decimal_places=2)
	humedad = models.DecimalField(max_digits=6,decimal_places=2)
	altitud = models.DecimalField(max_digits=6,decimal_places=2)
	luminosidad = models.DecimalField(max_digits=5,decimal_places=2)
	distanciaLinea = models.DecimalField(max_digits=5,decimal_places=2)

class simulacion(models.Model):
	nombre = models.CharField(max_length=50)
	lineaSiembra = models.IntegerField()
	estado = models.IntegerField()
	siembra = models.ForeignKey(siembra,null=True,blank=False,on_delete=models.CASCADE)
	fase = models.ManyToManyField(faseCultivo)
	confi = models.OneToOneField(configuracion)
	usu = models.ForeignKey(usuario,null=True,blank=False)
	def __str__(self):
		return self.nombre