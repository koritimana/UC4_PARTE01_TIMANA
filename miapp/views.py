from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Luis Montes Palacios </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    return render(request,'index.html', {
})

def carreras(request):
    return render(request,'carreras.html',{
})

def crear_curso(request):
    return render(request, 'crear_curso.html')

def carreras(request):
    return render(request,'carreras.html', {
    'titulo':'Estudiantes',
})
def crear_carrera(request):
    return render(request,'crear_carrera.html',{
})
