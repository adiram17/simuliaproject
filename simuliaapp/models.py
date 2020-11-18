from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Contact(models.Model):
    name = models.CharField(db_column='name', max_length=50, blank=False, verbose_name='Nama')
    phone = models.CharField(db_column='phone', max_length=20, blank=False, verbose_name='No HP')
    class Meta:
        db_table = 'contact'
        verbose_name = 'Kontak'
        verbose_name_plural = 'Kontak'
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Variety(models.Model):
    name = models.CharField(db_column='name', max_length=50, blank=False, verbose_name='Nama Varietas')
    description = models.TextField(db_column='description', max_length=200, blank=False, verbose_name='Deskripsi')
    class Meta:
        db_table = 'variety'
        verbose_name = 'Varietas'
        verbose_name_plural = 'Varietas'
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Serelia(models.Model):
    SEED_TYPES = [
        ('Benih Tetua', 'Benih Tetua'),
        ('Benih Inti', 'Benih Inti'),
        ('Benih Hibrida', 'Benih Hibrida'),
        ('Benih UPBS', 'Benih UPBS'),
    ]
    locationid = models.CharField(db_column='locationid', max_length=50, blank=False, verbose_name='Location ID')
    seed_type = models.CharField(db_column='seed_type', max_length=100, blank=False, choices=SEED_TYPES, verbose_name='Tipe Benih')
    address = models.TextField(db_column='address', max_length=1000, blank=False, verbose_name='Alamat')
    plant_date = models.DateField(db_column='plant_date', max_length=100, blank= True, null=True, verbose_name='Tanggal Tanam')
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, verbose_name='Varietas')
    area = models.IntegerField(db_column='area', blank=False, default=0, verbose_name='Luas Lahan')
    obstacle = models.TextField(db_column='obstacle',max_length=1000, blank=False, verbose_name='Kendala')
    cp_name = models.CharField(db_column='cp_name',max_length=100, blank=False, verbose_name='Contact Person')
    evidence = models.ImageField(upload_to='uploaded/evidence', verbose_name='Upload Image')
    created_date = models.DateField( blank=True, default=datetime.now, verbose_name='Tanggal Laporan')

    class Meta:
        db_table = 'serelia'
        verbose_name = 'Standing Crop Benih'
        verbose_name_plural = 'Standing Crop Benih'
    def __unicode__(self):
        return self.locationid
    def __str__(self):
        return self.locationid

@receiver(post_delete, sender=Serelia)
def serelia_delete(sender, instance, **kwargs):
    instance.evidence.delete(False) 

class Processing(models.Model):
    processingid = models.CharField(db_column='processingid', max_length=50, blank=False, verbose_name='Processing ID')
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, verbose_name='Varietas')
    in_date = models.DateField(db_column='in_date', max_length=100, blank= True, null=True, verbose_name='Tanggal Masuk')
    weight = models.IntegerField(db_column='weight', blank=False, default=0, verbose_name='Berat Tongkol (kg)')
    source = models.CharField(db_column='source', max_length=100, blank=False, verbose_name='Asal Benih')
    cp_name = models.TextField(db_column='cp_name',max_length=100, blank=False, verbose_name='Penanggung Jawab')
    out_date = models.DateField(db_column='out_date', max_length=100, blank= True, null=True, verbose_name='Tanggal Keluar')
    result = models.CharField(db_column='result',max_length=100, blank=False, verbose_name='Hasil Benih')
    evidence = models.ImageField(upload_to='uploaded/evidence', verbose_name='Upload Image')
    created_date = models.DateField( blank=True, default=datetime.now, verbose_name='Tanggal Laporan')

    class Meta:
        db_table = 'processing'
        verbose_name = 'Processing Benih'
        verbose_name_plural = 'Processing Benih'
    def __unicode__(self):
        return self.processingid
    def __str__(self):
        return self.processingid

@receiver(post_delete, sender=Processing)
def processing_delete(sender, instance, **kwargs):
    instance.evidence.delete(False) 

class Warehousestock(models.Model):
    stockid = models.CharField(db_column='stockid', max_length=50, blank=False, verbose_name='Stock ID')
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, verbose_name='Varietas')
    start_weight = models.IntegerField(db_column='start_weight', blank=False, default=0, verbose_name='Stok Awal (kg)')
    out_weight = models.IntegerField(db_column='out_weight', blank=False, default=0, verbose_name='Keluar (kg)')
    end_weight = models.IntegerField(db_column='end_weight', blank=False, default=0, verbose_name='Stok Akhir (kg)')
    created_date = models.DateField( blank=True, default=datetime.now, verbose_name='Tanggal Laporan')
    
    class Meta:
        db_table = 'warehousestock'
        verbose_name = 'Stok Gudang PS'
        verbose_name_plural = 'Stok Gudang PS'
    def __unicode__(self):
        return self.stockid
    def __str__(self):
        return self.stockid
