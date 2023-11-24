from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.username