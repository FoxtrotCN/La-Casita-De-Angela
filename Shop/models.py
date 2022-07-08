from django.contrib.auth.models import User
from django.db import models





class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=100)
    quantity = models.IntegerField("Quantity")
    image = models.ImageField("Image", upload_to='images/', null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        row = "Name: " + self.name + "-" + "Quantity: " + str(self.quantity)
        return row

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

