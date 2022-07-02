from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=100)
    quantity = models.IntegerField("Cantidad")
    image = models.ImageField("Imagen", upload_to='images/', null=False)
