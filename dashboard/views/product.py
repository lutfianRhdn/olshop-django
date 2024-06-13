from django.shortcuts import render, redirect
from product.models import Produk
# from category.models import Kategori
from dashboard.forms import productform
import os
from olshop.settings import BASE_DIR
def index(request):
    
    products = Produk.objects.all()
    return render(request, 'admin/products/index.html', {'products': products})

def create(request):
    form = productform()
    return render(request, 'admin/products/create.html', {'form': form})

def store(request):
  
    if request.method == 'POST':

        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('dashboard:products')
    # # with open(os.path.join(BASE_DIR, 'storage')+request.FILES['foto_produk'], 'wb+') as destination:
    #     for chunk in request.FILES['foto_produk'].chunks():
    #         destination.write(chunk)

def edit(request, id):
    if request.method == 'POST':
        product = Produk.objects.get(id_produk=id)
        forms = productform(request.POST, request.FILES, instance=product)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:products')
        else:
            return render(request, 'admin/products/update.html', {'form': forms, 'product': product})
    else:
        product = Produk.objects.get(id_produk=id)
        form = productform(instance=product)
        return render(request, 'admin/products/update.html', {'form': form, 'product': product})
def update(request, id):
    pass

def delete(request, id):
    Produk.objects.filter(id_produk=id).delete()
    return redirect('dashboard:products')

