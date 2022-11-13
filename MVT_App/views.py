from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")


def datos_familiares(request):

    archivo = open(r'C:\Users\Lemuc\Desktop\MVT_Bautista\MVT_Bautista\MVT_Bautista\templates\mvt.html')

    plantilla = Template(archivo.read())

    archivo.close()

    informacion_nombre =     ['Nombre: Bautista Cano',
     'Nombre: Alan Cano.',
     'Nombre: Cecilia Cace.',
    ]

    informacion_edad = ['Edad: 21',
    'Edad: 27',
    'Edad: 52',
    ]

    datos = {'informacion': informacion_nombre,'Edad': informacion_edad}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
