from django.db import models
from category.models import Kategori
# Create your models here.

class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    # id_kategori = models.IntegerField()
    nama_produk = models.CharField(max_length=100)
    harga_produk = models.IntegerField()
    berat_produk = models.IntegerField()
    foto_produk = models.CharField(max_length=100)
    deskripsi_produk = models.TextField()
    stok_produk = models.IntegerField()
    kategori = models.ForeignKey(Kategori, models.DO_NOTHING, db_column='id_kategori')

    class Meta:
        managed = False
        db_table = 'produk'


class ProdukFoto(models.Model):
    id_produk_foto = models.AutoField(primary_key=True)
    nama_produk_foto = models.CharField(max_length=255)
    produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='id_produk')
    
    class Meta:
        managed = False
        db_table = 'produk_foto'