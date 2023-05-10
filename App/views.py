from django.shortcuts import render, redirect

from datetime import datetime
from multiprocessing import context
from operator import is_not

from App.forms import Articuloform, Autorform, Categoriaform, Registrousuario
from App.models import Articulo, Autor, Categoria 
from django.http import HttpResponse



# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def formulario_articulos(request):
    if request.method == "GET":
        mi_formulario = Articuloform()
        contexto = {"formulario": mi_formulario}
        return render(request, "form-articulo.html", context = contexto)

    if request.method == "POST":

        mi_formulario = Articuloform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Articulo(
                titulo = mi_formulario_completado["titulo"],
                texto = mi_formulario_completado["texto"],
                fecha = mi_formulario_completado["fecha"],
            )
            nuevo_articulo.save()
            return render(request, "form_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "form-articulo.html", context = contexto)


def formulario_categoria(request):
    if request.method == "GET":

        mi_formulario = Categoriaform()
        contexto = {"formulario": mi_formulario}
        return render(request, "form-categoria.html", context = contexto)

    if request.method == "POST":

        mi_formulario = Categoriaform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Categoria(
                nombre = mi_formulario_completado["nombre"],
                fecha = mi_formulario_completado["fecha"],
            )
            nuevo_articulo.save()
            return render(request, "form_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "form-categoria.html", context = contexto)


def formulario_autores(request):
    if request.method == "GET":

        mi_formulario = Autorform()
        contexto = {"formulario": mi_formulario}
        return render(request, "form-autor.html", context = contexto)

    if request.method == "POST":

        mi_formulario = Autorform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Autor(
                nombre = mi_formulario_completado["nombre"],
                apodo = mi_formulario_completado["apodo"],
                profecion = mi_formulario_completado["profecion"],
                edad = mi_formulario_completado["edad"],
                mail = mi_formulario_completado["mail"],
            )
            nuevo_articulo.save()
            return render(request, "form_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "form-autor.html", context = contexto)

def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "form-busqueda-articulo.html")

    if request.method == "POST":
        titulo_a_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "result-busqueda-articulo.html", context = contexto)