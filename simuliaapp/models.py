from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Serelia(models.Model):
    VARIETY_CHOICES = [
        ('MAL03', 'MAL03'),
        ('G10', 'G10'),
        ('Contamination', 'Contamination'),
    ]
    locationid = models.CharField(db_column='locationid', max_length=50, blank=False, verbose_name='Location ID')
    address = models.TextField(db_column='address', max_length=1000, blank=False, verbose_name='Alamat')
    plant_date = models.DateField(db_column='plant_date', max_length=100, blank= True, null=True, verbose_name='Tanggal Tanam')
    variety = models.CharField(db_column='variety', max_length=100, blank=False, choices=VARIETY_CHOICES, verbose_name='Varietas')
    area = models.TextField(db_column='area',max_length=1000, blank=False, verbose_name='Area')
    obstacle = models.TextField(db_column='obstacle',max_length=1000, blank=False, verbose_name='Kendala')
    cp_name = models.CharField(db_column='cp_name',max_length=100, blank=False, verbose_name='Contact Person')
    evidence = models.ImageField(upload_to='uploaded/evidence', verbose_name='Upload Image')
    created_date = models.DateField( blank=True, default=datetime.now)

    class Meta:
        db_table = 'serelia'
        verbose_name = 'Serelia'
        verbose_name_plural = 'Serelias'
    def __unicode__(self):
        return self.locationid
    def __str__(self):
        return self.locationid

@receiver(post_delete, sender=Serelia)
def submission_delete(sender, instance, **kwargs):
    instance.evidence.delete(False) 
