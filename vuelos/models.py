from django.db import models

class Vuelo(models.Model):
    codigo=models.CharField(max_length=100)
    origen=models.CharField(max_length=100)
    destino=models.CharField(max_length=100)

    def __str__(self):
        return self.codigo

class Aerolinea(models.Model):
    nombre=models.CharField(max_length=100)
    pais_origen=models.CharField(max_length=100)
    vuelo=models.ForeignKey(Vuelo,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre