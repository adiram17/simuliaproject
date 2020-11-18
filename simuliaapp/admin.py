from django.contrib import admin
from .models import Serelia, Variety, Contact, Processing, Warehousestock
from import_export.admin import ExportActionMixin

@admin.register( Serelia)
class SereliaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('locationid', 'seed_type', 'created_date', 'area', 'address', 'plant_date', 'variety', 'obstacle', 'cp_name')
    
@admin.register(Processing)
class ProcessingAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('processingid', 'variety', 'created_date', 'in_date', 'weight', 'source', 'cp_name', 'out_date', 'result')
    
@admin.register(Warehousestock)
class WarehousestockAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('stockid', 'variety', 'created_date', 'start_weight', 'out_weight', 'end_weight')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')

@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')