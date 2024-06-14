from django.forms import ModelForm,ModelChoiceField,FileField,Select,FileInput
from django.utils.translation import gettext_lazy as _

from product.models import Produk
from category.models import Jenis

class productform(ModelForm):
    jenis = ModelChoiceField(queryset=Jenis.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    
    # foto_produk = FileField(widget=FileInput(attrs={'class': 'form-control'}),)
    # def __init__(self, *args, **kwargs):
    #     super(productform, self).__init__(*args, **kwargs)
    #     self.fields['jenis'].label_from_instance = lambda obj: obj.nama_kategori

    class Meta:
        model = Produk
        fields = ['kode', 'jenis', 'warna','merk', 'foto_produk','ketersediaan','jadwal']
        labels = {
            'kode': _('Kode Produk'),
            'jenis': _('Jenis Produk'),
            'warna': _('Warna Produk'),
            'merk': _('Merk Produk'),
            'foto_produk': _('Foto Produk'),
            'ketersediaan': _('Ketersediaan Produk'),
            'jadwal': _('Jadwal Produk'),
        }
        
     
    
      