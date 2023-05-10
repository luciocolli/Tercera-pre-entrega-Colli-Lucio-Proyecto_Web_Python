from django.contrib import admin
from django.urls import path, include


from App.views import (
    inicio,
    formulario_articulos,
    formulario_autores,
    formulario_categoria,
    buscar_articulo,
)

urlpatterns = [
    path("inicio/", inicio),
    path("inicio/form-articulo.html/", formulario_articulos),
    path("inicio/form-categoria.html/", formulario_categoria),
    path("inicio/form-autor.html/", formulario_autores),
    path("inicio/form-busqueda-articulo.html/", buscar_articulo),
]