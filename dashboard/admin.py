from django.contrib import admin

# # Register your models here.
from product.models import Produk
# class ProdukAdmin(admin.ModelAdmin):
#     list_display = ['nama_produk', 'harga_produk', 'berat_produk', 'deskripsi_produk','stok_produk', 'kategori']
#     list_filter = ['kategori']
#     search_fields = ['nama', 'kategori']
#     list_per_page = 10
#     list_editable = ['harga_produk', 'stok_produk']
    
# admin.site.register(Produk, ProdukAdmin)

# admin.site.site_header = 'Olshop Admin'
# admin.site.site_title = 'Olshop Admin'
# admin.site.index_title = 'Olshop Admin'
