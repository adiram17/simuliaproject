from django import forms
from django.forms import ModelForm
from .models import Serelia, Processing, Warehousestock

class SereliaForm(ModelForm):
    class Meta:
        model = Serelia
        fields = ('seed_type','address', 'plant_date', 'variety', 'area', 'obstacle', 'cp_name', 'evidence')
        widgets = {
            'seed_type': forms.Select(attrs={'class':'form-control  '}),
            'address': forms.TextInput(attrs={'class':'form-control  '}),
            'plant_date': forms.DateInput(attrs={'class':'form-control  ', 'id':'plant_date'}),
            'variety': forms.Select(attrs={'class':'form-control  '}),
            'area': forms.NumberInput(attrs={'class':'form-control  '}),
            'obstacle': forms.TextInput(attrs={'class':'form-control  '}),
            'cp_name': forms.TextInput(attrs={'class':'form-control  '}),
            'evidence': forms.FileInput(),
        }

class ProcessingForm(ModelForm):
    class Meta:
        model = Processing
        fields = ('variety','in_date', 'weight', 'source', 'cp_name', 'out_date', 'result', 'evidence')
        widgets = {
            'variety': forms.Select(attrs={'class':'form-control  '}),
            'in_date': forms.DateInput(attrs={'class':'form-control  ', 'id':'in_date'}),
            'weight': forms.NumberInput(attrs={'class':'form-control  '}),
            'source': forms.TextInput(attrs={'class':'form-control  '}),
            'cp_name': forms.TextInput(attrs={'class':'form-control  '}),
            'out_date': forms.DateInput(attrs={'class':'form-control  ', 'id':'out_date'}),
            'result': forms.TextInput(attrs={'class':'form-control  '}),
            'evidence': forms.FileInput(),
        }

class WarehousestockForm(ModelForm):
    class Meta:
        model = Warehousestock
        fields = ('variety','start_weight', 'out_weight', 'end_weight')
        widgets = {
            'variety': forms.Select(attrs={'class':'form-control  '}),
            'start_weight': forms.NumberInput(attrs={'class':'form-control  '}),
            'out_weight': forms.NumberInput(attrs={'class':'form-control  '}),
            'end_weight': forms.NumberInput(attrs={'class':'form-control  '}),
            
            
        }