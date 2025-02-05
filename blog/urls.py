from django.urls import path
from blog.views import inicio, saludo

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('saludo/<nombre>/<apellido>/', saludo, name= "Saludo")
]