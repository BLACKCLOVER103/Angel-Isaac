from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
# Create your views here.
def fondo(request):
    externo = open("C:/Users/PC/Desktop/examenu3/templates/index.html")
    plantilla = Template(externo.read())
    externo.close()
    ctx = Context()
    contenido = plantilla.render(ctx)
    return HttpResponse(contenido)
# Create your views here.
