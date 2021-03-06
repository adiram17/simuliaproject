# Generated by Django 2.2.5 on 2020-11-18 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simuliaapp', '0008_auto_20201118_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processing',
            name='weight',
            field=models.IntegerField(db_column='weight', verbose_name='Berat Tongkol (kg)'),
        ),
        migrations.AlterField(
            model_name='serelia',
            name='area',
            field=models.IntegerField(db_column='area', verbose_name='Luas Lahan'),
        ),
        migrations.AlterField(
            model_name='serelia',
            name='variety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuliaapp.Variety', verbose_name='Varietas'),
        ),
        migrations.AlterField(
            model_name='variety',
            name='name',
            field=models.CharField(db_column='name', max_length=50, verbose_name='Nama Varietas'),
        ),
        migrations.AlterField(
            model_name='warehousestock',
            name='end_weight',
            field=models.IntegerField(db_column='end_weight', verbose_name='Stok Akhir (kg)'),
        ),
        migrations.AlterField(
            model_name='warehousestock',
            name='out_weight',
            field=models.IntegerField(db_column='out_weight', verbose_name='Keluar (kg)'),
        ),
        migrations.AlterField(
            model_name='warehousestock',
            name='start_weight',
            field=models.IntegerField(db_column='start_weight', verbose_name='Stok Awal (kg)'),
        ),
    ]
