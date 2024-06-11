from django.forms import ModelForm,ModelChoiceField
from django.utils.translation import gettext_lazy as _

from product.models import Produk
from category.models import Kategori

class productform(ModelForm):
    kategori = ModelChoiceField(
      queryset=Kategori.objects.all(),
      to_field_name='nama_kategori', 
      label=_('Kategori'),
      empty_label=_('Select Kategori'))
    
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga_produk', 'berat_produk','deskripsi_produk','stok_produk','kategori','foto_produk']
        labels = {
            'nama_produk': _('Nama Produk'),
            'harga_produk': _('Harga Produk'),
            'berat_produk': _('Berat Produk'),
            'deskripsi_produk': _('Deskripsi Produk'),
            'stok_produk': _('Stok Produk'),
            'kategori': _('Kategori'),
            'foto_produk': _('Foto Produk')
        }
        
        help_texts = {
            'nama_produk': _('Nama Produk'),
            'harga_produk': _('Harga Produk'),
            'berat_produk': _('Berat Produk'),
            'deskripsi_produk': _('Deskripsi Produk'),
            'stok_produk': _('Stok Produk'),
            'kategori': _('Kategori'),
            'foto_produk': _('Foto Produk')
        }
        
        error_messages = {
            'nama_produk': {
                'max_length': _("Nama Produk terlalu panjang."),
                'required': 'Nama Produk harus diisi.'
            },
            'harga_produk': {
                'max_length': _("Harga Produk terlalu panjang."),
                'required': 'Harga Produk harus diisi.'
            },
            'berat_produk': {
                'max_length': _("Berat Produk terlalu panjang."),
                'required': 'Berat Produk harus diisi.'
            },
            'deskripsi_produk': {
                'max_length': _("Deskripsi Produk terlalu panjang."),
                'required': 'Deskripsi Produk harus diisi.'
            },
            'stok_produk': {
                'max_length': _("Stok Produk terlalu panjang."),
                'required': 'Stok Produk harus diisi.'
            },
            'kategori': {
                'max_length': _("Kategori terlalu panjang."),
                'required': 'Kategori harus diisi.'
            },
            'foto_produk': {
                'max_length': _("Foto Produk terlalu panjang."),
                'required': 'Foto Produk harus diisi. '
            },
        }
      