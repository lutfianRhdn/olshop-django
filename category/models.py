from django.db import models


# Create your models here.

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kategori'
