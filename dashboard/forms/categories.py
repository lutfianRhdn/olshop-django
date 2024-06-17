from django.forms import ModelForm,ModelChoiceField,FileField,Select,FileInput
from django.utils.translation import gettext_lazy as _

from category.models import Jenis

class categoriesForm(ModelForm):    
    class Meta:
        model = Jenis
        fields = ["kode", "jenis", "berat", "kapasitas", "daya_mesin"]
        labels = {
            'kode': _('Kode'),
            'jenis': _('Jenis'),
            'berat': _('Berat'),
            'kapasitas': _('Kapasitas'),
            'daya_mesin': _('Daya Mesin'),
        }
        
     
    
      