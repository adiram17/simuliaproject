from django import forms

class SereliaForm(forms.Form):
    sereliaid = forms.CharField(label='ID', widget=forms.TextInput(attrs={'class': 'form-control mb-2' ,'value':'L001', 'readonly':'true'}))
    variety = forms.CharField(label='Varietas', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    address = forms.CharField(label='Alamat', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    area = forms.CharField(label='Luas lahan', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    plant_date = forms.CharField(label='Tanggal Tanam', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    obstacle = forms.CharField(label='Kendala', widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))

    #variety = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #plant_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #obstacle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #contact_person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #changed_by = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
