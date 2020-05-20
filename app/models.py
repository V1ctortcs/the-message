# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    telefone = models.CharField(max_length=12, unique=True)
    data_ciacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    # FK de User do django
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_model'

    def __str__(self):
        return str(self.id)