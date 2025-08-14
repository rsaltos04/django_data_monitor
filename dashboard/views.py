from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    total_puentes = 0
    total_coronas = 0
    total_protesis = 0
    
    total_mañana = 0
    total_tarde = 0

    emails_horarios = []

    
    for reserva in posts.values():

        email = reserva.get("email", "Sin email")
        horario = reserva.get("horario", "Sin horario")
        emails_horarios.append({"email": email, "horario": horario})

        servicios = reserva.get("servicios", [])  # Accede a la lista de servicios
        if "coronas" in servicios:
            total_coronas += 1
        if "protesis" in servicios:
            total_protesis += 1
        if "puentes" in servicios:
            total_puentes += 1
        horario = reserva.get("horario", "")
        if horario == "Manana":
            total_mañana += 1
        elif horario == "Tarde":
            total_tarde += 1

    # Número total de respuestas
    total_responses = len(posts)
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'total_coronas': total_coronas,
        'total_protesis': total_protesis,
        'total_puentes': total_puentes,
        'total_mañana': total_mañana,  
        'total_tarde': total_tarde, 
        'horarios_labels': ["Manana", "Tarde"],
        'emails_horarios': emails_horarios,  # Lista de emails y horarios
        'horarios_values': [total_mañana, total_tarde],
        'posts': posts
    }

    return render(request, 'dashboard/index.html', data)