from django.shortcuts import render,HttpResponse
from .models import Produk
from django.http import JsonResponse


# Create your views here.
def show_products(request):
    produk = Produk.objects.all()
    return render(request, 'products/index.html', {'products': produk})

def product_detail(request,kode):
    produk = Produk.objects.get(kode=kode)
    return render(request,'products/detail.html',{'product':produk})

def get_all_calendar_event(request):
    start= request.GET.get('start',"")
    end= request.GET.get('end',"")
    
    products= Produk.objects.filter(jadwal__range=[start, end])
    # 'title'=>'Phasellus ac arcu in tortor faucibus pharetra','start'=>$year.'-'.$month.'-21','end'=>$year.'-'.$month.'-25','className'=>'red'
    
    result =[]
    for product in products:
        color = "yellow"
        if product.warna =='Kuning':
            color="yellow"
        elif product.warna =='Merah':
            color="red"
        elif product.warna =='Orange':
            color="orange"
        
        result.append({
            'title':f"{product.jenis.kode}-{product.jenis.jenis}-{product.warna}-{product.merk}",
            'start':f"{product.jadwal.year}-{product.jadwal.month}-{product.jadwal.day}",
            'end':product.jadwal,
            'className':color})
    return JsonResponse(result,safe=False)
    # add this
    # print(products)