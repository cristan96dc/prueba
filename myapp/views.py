from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'home.html')

def productos_view(request):
    query = request.GET.get('q')
    tipo_filter = request.GET.get('tipo')

    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)
    
    if tipo_filter:
        productos = productos.filter(tipo=tipo_filter)
    
    # Obtener los tipos únicos de productos para el filtro
    tipos = Producto.objects.values_list('tipo', flat=True).distinct()

    return render(request, 'productos.html', {'productos': productos, 'tipos': tipos})



def custom_page_not_found_view(request, exception):
    return render(request, '404.html', {}, status=404)

def ok_view(request):
    return render(request, 'ok.html')