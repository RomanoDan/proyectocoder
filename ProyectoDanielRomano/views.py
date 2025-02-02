from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a la primer prueba de Django."}
    return render(request, "ProyectoDanielRomano/index.html", context)