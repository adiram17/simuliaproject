from django.contrib import admin
from .models import Serelia

# Register your models here.
class SereliaAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'address', 'plant_date', 'variety')
    
admin.site.register(Serelia, SereliaAdmin)