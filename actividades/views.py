from django.shortcuts import render
from .models import Actividad
from django.shortcuts import get_object_or_404
from .forms import ActividadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required ( login_url = '/login/' )
def lista_actividades(request):

    a = Actividad.objects.all()


    return render(request, 'actividades/lista_actividades.html', {'a':a})

@login_required ( login_url = '/login/' )
def detalle_actividad(request, id_actividad):

    b = get_object_or_404(Actividad, pk=id_actividad)

    return render(request, 'actividades/detalle_actividad.html', {'b':b})

@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def nueva_actividad(request):

    form_actividad = ActividadForm()

    if request.method == "POST":
        form_actividad = ActividadForm(request.POST)

        if form_actividad.is_valid():
            form_actividad.save()
            return render(request, "actividades/nueva_actividad_mesaje.html")

    return render(request,"actividades/nueva_actividad_form.html", {"form_actividad":form_actividad})

def agregar_servicios (request):

        return render (request, 'actividades/agregar_servicios.html',)

def lista_servicio (request):

    return render (request, 'actividades/forms/lista_servicios.html',)

def agregar_actividad(request):

    c = Actividad.objects.all()

    return render(request, 'actividades/agregar.html', {'c':c})

def servicio_actividad(request):

    f = Actividad.objects.all()

    return render(request, 'actividades/forms/servicio.html', {'f':f})

def tipo_actividad(request):

    g = Actividad.objects.all()

    return render(request, 'actividades/forms/tipo.html', {'g':g})
