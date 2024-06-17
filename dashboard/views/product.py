from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from product.models import Produk
# from category.models import Kategori
from dashboard.forms import productform
import os
from olshop.settings import BASE_DIR

def index(request):
    
    products = Produk.objects.all()
    products = {
        'products': products
    }
    
    return render(request, 'admin/products/index.html', products)

def create(request):
    form = productform()
    return render(request, 'admin/products/create.html', {'form': form})

def store(request):
  
    if request.method == 'POST':

        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('dashboard:products')

def edit(request, id):
    
    Produk_ins = Produk.objects.get(kode=id)
    form = productform(instance=Produk_ins)
    
    if request.method == 'POST':
        form = productform(request.POST, request.FILES, instance=Produk_ins)
        if form.is_valid():
            form.save()
            return redirect('dashboard:products')
    else:
        form = productform(instance=Produk_ins)
    
    return render(request, 'admin/products/update.html', {'form': form, 'product': Produk_ins})


def delete(request, id):
    Produk_ins = Produk.objects.get(kode=id)
    Produk_ins.delete()

    return redirect('dashboard:products')

