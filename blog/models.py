from importlib.resources import contents
from turtle import title
from django.db import models

# CADA VEZ QUE SE REALICE UN CAMBIO EN ESTE ARCHIVO SE DEBE RENOVER LAS MIGRACIONES: * PYTHON MANAGE.PY MIGRATRION BLOG *

class Post(models.Model):
    title= models.CharField(max_length=250)
    contents=models.TextField()


    def __str__(self):

        return self.title