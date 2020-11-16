from django import forms
from django.forms import ModelForm
from .models import Serelia

class SereliaForm(ModelForm):
    class Meta:
        model = Serelia
        fields = ('seed_type','address', 'plant_date', 'variety', 'area', 'obstacle', 'cp_name', 'evidence')
        labels = {
            'seed_type':'Tipe Benih',
            'address':'Alamat',
            'plant_date':'Tanggal Tanam',
            'variety':'Varietas',
            'area':'Luas lahan (ha)',
            'obstacle':'Kendala',
            'cp_name':'Contact Person',
            'evidence':'Upload Foto'
        }
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