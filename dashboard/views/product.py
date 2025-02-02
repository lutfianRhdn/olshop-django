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
def calendar(request):
    return render(request,'products/calendar.html')
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


from django.views import generic


class ProdukListView(generic.ListView):
    model = Produk
    context_object_name ="products"
    template_name = 'admin/products/index.html'
    
class ProdukDetailView(generic.DetailView):
    model = Produk
    template_name = 'admin/products/detail.html'

class ProdukCreateView(generic.CreateView):
    model = Produk
    form_class = productform
    template_name = 'admin/products/create.html'
    fields = '__all__'
    
class ProdukUpdateView(generic.UpdateView):
    model = Produk
    form_class = productform
    template_name = 'admin/products/update.html'
    fields = '__all__'
    
class ProdukDeleteView(generic.DeleteView):
    model = Produk
    # template_name = 'admin/products/delete.html'
    success_url = '/dashboard/products/'
    
