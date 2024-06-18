from django.db import models

# Create your models here.

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nama_lengkap = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'admin'
        
        