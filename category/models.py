from django.db import models


# Create your models here.

class Jenis(models.Model):
    kode = models.CharField(db_column='Kode', max_length=50, blank=True, unique=True,primary_key=True)  # Field name made lowercase.
    jenis = models.CharField(db_column='Jenis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    berat = models.CharField(db_column='Berat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kapasitas = models.CharField(db_column='Kapasitas', max_length=50, blank=True, null=True)  # Field name made lowercase.    
    daya_mesin = models.CharField(db_column='Daya Mesin', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'jenis'