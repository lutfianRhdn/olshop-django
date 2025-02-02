from django.db import models
from category.models import Jenis
# Create your models here.


class Produk(models.Model):
    kode = models.CharField(db_column='Kode', max_length=50, blank=True, primary_key=True)  # Field name made lowercase.
    # jenis = models.CharField(db_column='Jenis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warna = models.CharField(db_column='Warna', max_length=50, blank=True, null=True)  # Field name made lowercase.
    merk = models.CharField(db_column='Merk', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ketersediaan = models.CharField(db_column='Ketersediaan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jadwal = models.DateField(db_column='Jadwal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notifikasi = models.BooleanField(db_column='Notifikasi', blank=True, null=True)  # Field name made lowercase.
    foto_produk = models.ImageField(db_column='Foto Produk', blank=True,null=True)
    jenis = models.ForeignKey(Jenis, models.DO_NOTHING, db_column='Jenis',to_field="kode")

    class Meta:
        managed = False
        db_table = 'produk'

