from django import forms
from django.forms import ModelForm
from .models import Serelia

class SereliaForm(ModelForm):
    class Meta:
        model = Serelia
        fields = ('address', 'plant_date', 'variety', 'area', 'obstacle', 'cp_name', 'evidence')
        labels = {
            'address':'Alamat',
            'plant_date':'Tanggal Tanam',
            'variety':'Varietas',
            'area':'Luas lahan (ha)',
            'obstacle':'Kendala',
            'cp_name':'Contact Person',
            'evidence':'Upload Foto'
        }
        widgets = {
            'address': forms.Textarea(attrs={'class':'form-control mb-2','rows': 3}),
            'plant_date': forms.DateInput(attrs={'class':'form-control mb-2', 'id':'plant_date'}),
            'variety': forms.Select(attrs={'class':'form-control mb-2'}),
            'area': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'obstacle': forms.Textarea(attrs={'class':'form-control mb-2', 'rows': 3}),
            'cp_name': forms.Textarea(attrs={'class':'form-control mb-2', 'rows': 3}),
            'evidence': forms.FileInput(),
        }