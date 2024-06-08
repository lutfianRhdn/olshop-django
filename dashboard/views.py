from django.shortcuts import render

def show_products(request):
    return render(request, 'admin/products/index.html')