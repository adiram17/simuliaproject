from django import forms
from django.forms import ModelForm
from .models import Serelia, Processing, Warehousestock

class SereliaForm(ModelForm):
    class Meta:
        model = Serelia
        fields = ('seed_type','address', 'plant_date', 'variety', 'area', 'obstacle', 'cp_name', 'evidence')
        widgets = {
            'seed_type': forms.Select(attrs={'class':'form-control mb-1'}),
            'address': forms.Textarea(attrs={'class':'form-control mb-1','rows': 2}),
            'plant_date': forms.DateInput(attrs={'class':'form-control mb-1', 'id':'plant_date'}),
            'variety': forms.Select(attrs={'class':'form-control mb-1'}),
            'area': forms.NumberInput(attrs={'class':'form-control mb-1'}),
            'obstacle': forms.Textarea(attrs={'class':'form-control mb-1', 'rows': 2}),
            'cp_name': forms.Textarea(attrs={'class':'form-control mb-1', 'rows': 2}),
            'evidence': forms.FileInput(),
        }

class ProcessingForm(ModelForm):
    class Meta:
        model = Processing
        fields = ('variety','in_date', 'weight', 'source', 'cp_name', 'out_date', 'result', 'evidence')
        widgets = {
            'variety': forms.Select(attrs={'class':'form-control mb-1'}),
            'in_date': forms.DateInput(attrs={'class':'form-control mb-1', 'id':'in_date'}),
            'weight': forms.NumberInput(attrs={'class':'form-control mb-1'}),
            'source': forms.TextInput(attrs={'class':'form-control mb-1'}),
            'cp_name': forms.Textarea(attrs={'class':'form-control mb-1', 'rows': 2}),
            'out_date': forms.DateInput(attrs={'class':'form-control mb-1', 'id':'out_date'}),
            'result': forms.TextInput(attrs={'class':'form-control mb-1'}),
            'evidence': forms.FileInput(),
        }

class WarehousestockForm(ModelForm):
    class Meta:
        model = Warehousestock
        fields = ('variety','start_weight', 'out_weight', 'end_weight')
        widgets = {
            'variety': forms.Select(attrs={'class':'form-control mb-1'}),
            'start_weight': forms.NumberInput(attrs={'class':'form-control mb-1'}),
            'out_weight': forms.NumberInput(attrs={'class':'form-control mb-1'}),
            'end_weight': forms.NumberInput(attrs={'class':'form-control mb-1'}),
            
            
        }