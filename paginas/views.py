from django.http import HttpResponse


def vista_inicio(request):
    return HttpResponse("Hello, World!")


def vista_acerca_de(request):
    return HttpResponse("Acerca de: esta es mi primera aplicación en Django.")
