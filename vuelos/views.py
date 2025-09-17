from django.shortcuts import render, redirect, get_object_or_404
from .models import Vuelo,Aerolinea
from .form import VueloForm ,AerolineaForm
# Create your views here.

def vuelo_list(request):
    vuelos=Vuelo.objects.all()
    return render(request, 'vuelos/vuelo_list.html',{'vuelos':vuelos})


def vuelo_crear(request):
    if request.method == "POST":
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vuelo_list")
    else:
        form = VueloForm()
    return render(request, "vuelos/crear.html", {"form": form})

def vuelo_editar(request, id):
    producto = get_object_or_404(Vuelo, id=id)
    if request.method == "POST":
        form = VueloForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("vuelo_list")
    else:
        form = VueloForm(instance=producto)
    return render(request, "vuelos/editar.html", {"form": form})

def eliminar_producto(request, id):
    vuelo = get_object_or_404(Vuelo, id=id)
    if request.method == "POST":
        vuelo.delete()
        return redirect("vuelo_list")
    return render(request, "vuelos/eliminar.html", {"vuelo": vuelo})

def buscar_producto(request):
    query = request.GET.get("q")
    resultados = Vuelo.objects.filter(nombre__icontains=query) if query else []
    return render(request, "vuelos/buscar.html", {"resultados": resultados})