from django.db import models

# Create your models here.
billeteras = [
        ("tigo-349", "tigo-349"),
        ("tigo-757", "tigo-757"),
        ("tigo-722", "tigo-722"),
        ("zimple-349", "zimple-349"),
        ("zimple-757", "zimple-757"),
        ("zimple-722", "zimple-722"),
        ("wally-349", "wally-349"),
        ("wally-757", "wally-757"),
        ("wally-722", "wally-722"),
    ]

class Giros(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    agregado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    billetera = models.CharField(max_length=100, choices=billeteras)
    monto = models.IntegerField()
    ref = models.CharField(max_length=100,blank=True)
    girosImg = models.ImageField(upload_to='giros/', null=True, blank=True)

    def __str__(self) ->str:
        return f"{self.cliente} -- {self.billetera} -- {self.monto}"
    


class Interfisa(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    agregado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    monto = models.IntegerField()
    interfisaImg = models.ImageField(upload_to='interfisa/', null=True, blank=True)

    def __str__(self) ->str:
        return f"{self.cliente}-{self.monto}"