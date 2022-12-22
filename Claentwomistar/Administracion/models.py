from django.db import models


class DetalleProductos(models.Model):
    id = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=25)
    Descripcion = models.TextField(max_length=250)
    Modelo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.Marca
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Valor = models.IntegerField()
    Stock = models.IntegerField()
    Ventas = models.IntegerField()
    DetalleProductos = models.ForeignKey(DetalleProductos, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)+" "+self.Nombre