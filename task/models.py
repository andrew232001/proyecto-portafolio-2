from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Puedes considerar el uso de campos más seguros, como models.PasswordField

    def __str__(self):
        return self.username