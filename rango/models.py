from django.db import models

class Bares(models.Model):
    nombre= models.CharField(max_length=25, unique=True)
    direccion = models.CharField(max_length=100)
    visitas = models.IntegerField(default=0)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre

class Tapas(models.Model):
    bar = models.ForeignKey(Bares)
    nombre= models.CharField(max_length=25, unique=True)
    votos = models.IntegerField(default=0)
    

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre
