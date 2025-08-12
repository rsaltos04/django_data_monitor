from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings

# Create your views here.


def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON
    # Número total de respuestas
    total_responses = len(posts)
    #tal vez hacer for al posts
    #tal que por reserva en post se buscan los servicios
    #por servicios en reserva se hacen 3 variables
    # si existe el servicio en servicios, se le suma 1 a la variable, caso contrario, se siquie nomás
    # de ahí, devolver eso en data
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }


    return render(request, 'dashboard/index.html', data)


