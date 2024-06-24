from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from category.models import Jenis
from dashboard.forms import categoriesForm
import os
from django.core.cache import cache




def index_categories(request):
    categories = Jenis.objects.all()
    cache.add("CATEGORY", categories, 60*60*24 )# 1 hari
    print(cache.get("CATEGORY"))
    categories = {
        'categories': categories
    }
    
    
    return render(request, 'admin/categories/index.html', categories)

def create_categories(request):
    form = categoriesForm()
    return render(request, 'admin/categories/create.html', {'form': form})
    
def edit_categories(request, id):
    
    Categories_ins = Jenis.objects.get(kode=id)
    form = categoriesForm(instance=Categories_ins)
    
    if request.method == 'POST':
        form = categoriesForm(request.POST, request.FILES, instance=Categories_ins)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    else:
        form = categoriesForm(instance=Categories_ins)
    
    return render(request, 'admin/categories/update.html', {'form': form, 'product': Categories_ins})


def delete_categories(request, id):
    Categories_ins = Jenis.objects.get(kode=id)
    Categories_ins.delete()

    return redirect('dashboard:categories')

def store_categories(request):
    if request.method == 'POST':

        form = categoriesForm(request.POST, request.FILES)
        cache.add("CATEGORY", form)
        
        if form.is_valid():
            form.save()
    return redirect('dashboard:categories')
    # # with open(os.path.join(BASE_DIR, 'storage')+request.FILES['foto_produk'], 'wb+') as destination:
    #     for chunk in request.FILES['foto_produk'].chunks():
    #         destination.write(chunk)