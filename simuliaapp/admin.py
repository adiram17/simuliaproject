from django.contrib import admin
from .models import Serelia

# Register your models here.
class SereliaAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'seed_type', 'created_date', 'area', 'address', 'plant_date', 'variety', 'obstacle', 'cp_name')
    
admin.site.register(Serelia, SereliaAdmin)