from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rango.models import Bares,Tapas
from rango.forms import TapasForm

def index(request):
    lista_bares = Bares.objects.order_by('-nombre')[:5]
    lista_tapas=Tapas.objects.order_by('-nombre')[:5]
    context_dict={'bares': lista_bares,'tapas': lista_tapas}
    return render(request, 'rango/index.html', context_dict)

def bares(request, bares_name_slug):
    context_dict = {}
    try:
        bares = Bares.objects.get(nombre=bares_name_slug)
        context_dict['bares_name'] = bares.nombre
        tapas = Tapas.objects.filter(bar=bares)
        context_dict['tapas'] = tapas
        context_dict['bares'] = bares
        bares.visitas=bares.visitas+1
        bares.save()
    except Bares.DoesNotExist:
        pass
    return render(request, 'rango/bares.html', context_dict)
def about(request):
   return render(request, 'rango/about.html')

def add_tapa(request):
    if request.method == 'POST':
        form = TapasForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form =TapasForm()

    return render(request, 'rango/new_tapa.html', {'form': form})
def reclama_datos (request):
    
    top_bares = Bares.objects.order_by('-visitas')[:3]
    datos={'lista_bares':[top_bares[0].nombre,top_bares[1].nombre,top_bares[2].nombre], 'lista_visitas':[top_bares[0].visitas,top_bares[1].visitas,top_bares[2].visitas]} 
    return JsonResponse(datos, safe=False)