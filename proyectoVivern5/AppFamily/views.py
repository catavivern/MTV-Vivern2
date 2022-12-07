from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.
def family(request):
    dictF1=FamiliarMayor(nombre="Virginia", apellido="Esc", edad=47, nacimiento=6/28/1975)
    dictF1.save()    
    cadena_texto1=f"familiar1 guadrado: Nombre: {dictF1.nombre}, Apellido:{dictF1.apellido}, Edad:{dictF1.edad}, Nacimiento:{dictF1.nacimiento}"

    dictF2=FamiliarMayor(nombre="Pablo", apellido="Esc", edad=51, nacimiento=8/5/1971)
    dictF2.save() 
    cadena_texto2=f"familiar2 guadrado: Nombre: {dictF2.nombre}, Apellido:{dictF2.apellido}, Edad:{dictF2.edad}, Nacimiento:{dictF2.nacimiento}"

    dictF3=FamiliarMayor(nombre="Bautista", apellido="Esc", edad=18, nacimiento=8/5/2004)
    dictF3.save() 
    cadena_texto3=f"familiar3 guadrado: Nombre: {dictF3.nombre}, Apellido:{dictF3.apellido}, Edad:{dictF3.edad}, Nacimiento:{dictF3.nacimiento}"

    template=loader.get_template("template1.html")

    documento=template.render(Context)
    
    return HttpResponse(documento)


