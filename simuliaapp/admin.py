from django.contrib import admin
from .models import Serelia, Variety, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
admin.site.register(Contact, ContactAdmin)

class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Variety, VarietyAdmin)

class SereliaAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'seed_type', 'created_date', 'area', 'address', 'plant_date', 'variety', 'obstacle', 'cp_name')
admin.site.register(Serelia, SereliaAdmin)

