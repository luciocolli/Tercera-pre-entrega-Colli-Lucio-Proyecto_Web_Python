from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length = 30)
    user = models.CharField(max_length = 30)

    def __str__(self):
        return self.user
    
class Articulo(models.Model):
    titulo = models.CharField(max_length = 30)
    texto = models.CharField(max_length = 1000)
    fecha = models.DateField(null = True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    cate = models.CharField(max_length = 50)

    def __str__(self):
        return self.cate

