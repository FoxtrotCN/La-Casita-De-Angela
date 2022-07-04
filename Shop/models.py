from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=100)
    quantity = models.IntegerField("Cantidad")
    image = models.ImageField("Imagen", upload_to='images/', null=False)

    # def __str__(self):
    #     row = "Nombre: " + self.name + "-" + "Cantidad: " + str(self.quantity)
    #     return row

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
