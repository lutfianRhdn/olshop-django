from django.db import models

# Create your models here.

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nama_lengkap = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'admin'
        
        
class Pelanggan(models.Model):
    id_pelanggan = models.AutoField(primary_key=True)
    email_pelanggan = models.CharField(max_length=100)
    password_pelanggan = models.CharField(max_length=50)
    nama_pelanggan = models.CharField(max_length=100)
    telepon_pelanggan = models.CharField(max_length=100)
    alamat_pelanggan = models.TextField()

    class Meta:
        managed = False
        db_table = 'pelanggan'