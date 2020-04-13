from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    dataNasc = models.DateField
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'users'