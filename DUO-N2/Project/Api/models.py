from django.db import models

# Create your models here.
class Productos(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=25)
    Precio=models.FloatField()
    Cantidad=models.IntegerField()
    Descripcion=models.TextField(max_length=70)
    Fecha=models.DateField()
    Categoria=models.TextField(max_length=50)
    imagen=models.ImageField(upload_to='Productos', null=True)

    def __str__(self):
        return self.Nombre