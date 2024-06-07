from django.db import models

# Create your models here.


class Pembayaran(models.Model):
    id_pembayaran = models.AutoField(primary_key=True)
    id_pembelian = models.IntegerField()
    nama = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    tanggal = models.DateField()
    bukti = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pembayaran'


class Pembelian(models.Model):
    id_pembelian = models.AutoField(primary_key=True)
    id_pelanggan = models.IntegerField()
    tanggal_pembelian = models.DateField()
    total_pembelian = models.IntegerField()
    alamat_pengiriman = models.TextField()
    status_pembelian = models.CharField(max_length=100)
    resi_pengiriman = models.CharField(max_length=50)
    totalberat = models.IntegerField()
    provinsi = models.CharField(max_length=255)
    distrik = models.CharField(max_length=255)
    tipe = models.CharField(max_length=255)
    kodepos = models.CharField(max_length=255)
    ekspedisi = models.CharField(max_length=255)
    paket = models.CharField(max_length=255)
    ongkir = models.IntegerField()
    estimasi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pembelian'


class PembelianProduk(models.Model):
    id_pembelian_produk = models.AutoField(primary_key=True)
    id_pembelian = models.IntegerField()
    id_produk = models.IntegerField()
    jumlah = models.IntegerField()
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()
    berat = models.IntegerField()
    subberat = models.IntegerField()
    subharga = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pembelian_produk'
