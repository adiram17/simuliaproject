# Generated by Django 2.2.5 on 2020-11-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serelia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationid', models.CharField(db_column='locationid', max_length=50, verbose_name='Location ID')),
                ('address', models.TextField(db_column='address', max_length=1000, verbose_name='Alamat')),
                ('plant_date', models.DateField(blank=True, db_column='plant_date', max_length=100, null=True, verbose_name='Tanggal Tanam')),
                ('variety', models.CharField(choices=[('MAL03', 'MAL03'), ('G10', 'G10'), ('Contamination', 'Contamination')], db_column='variety', max_length=100, verbose_name='Varietas')),
                ('area', models.TextField(db_column='area', max_length=1000, verbose_name='Area')),
                ('obstacle', models.TextField(db_column='obstacle', max_length=1000, verbose_name='Kendala')),
                ('cp_name', models.CharField(db_column='cp_name', max_length=100, verbose_name='Contact Person')),
                ('evidence', models.ImageField(upload_to='uploaded/evidence', verbose_name='Upload Image')),
            ],
            options={
                'verbose_name': 'Serelia',
                'verbose_name_plural': 'Serelias',
                'db_table': 'serelia',
            },
        ),
    ]
