from django.db import models

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Valor = models.IntegerField()
    Stock = models.IntegerField()
    Ventas = models.IntegerField(default=0)
    Marca = models.CharField(max_length=25)
    Descripcion = models.TextField(max_length=250)
    Modelo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.Nombre