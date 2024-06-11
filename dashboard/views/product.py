from django.shortcuts import render
from product.models import Produk
from dashboard.forms import productform
def index(request):
    
    products = Produk.objects.all()
    return render(request, 'admin/products/index.html', {'products': products})

def create(request):
    form = productform()
    return render(request, 'admin/products/create.html', {'form': form})

def store(request):
    pass

def edit(request, id):
    return render(request, 'admin/products/update.html')

def update(request, id):
    pass

def delete(request, id):
    return render(request, 'admin/products/delete.html')

