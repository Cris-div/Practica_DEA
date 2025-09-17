from django.shortcuts import render
from .models import Vuelo,Aerolinea
# Create your views here.

def vuelo_list(request):
    vuelos=Vuelo.objects.all()
    return render(request, 'vuelo/vuelo_list.html',{'vuelos':vuelos})
