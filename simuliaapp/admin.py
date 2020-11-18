from django.contrib import admin
from .models import Serelia, Variety, Contact, Processing, Warehousestock
import csv
from django.http import HttpResponse

actions = ["export_as_csv"]

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
admin.site.register(Contact, ContactAdmin)

class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Variety, VarietyAdmin)

class SereliaAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('locationid', 'seed_type', 'created_date', 'area', 'address', 'plant_date', 'variety', 'obstacle', 'cp_name')
    actions = ["export_as_csv"]
admin.site.register(Serelia, SereliaAdmin)

class ProcessingAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('processingid', 'variety', 'created_date', 'in_date', 'weight', 'source', 'cp_name', 'out_date', 'result')
    actions = ["export_as_csv"]
admin.site.register(Processing, ProcessingAdmin)

class WarehousestockAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('stockid', 'created_date', 'start_weight', 'out_weight', 'end_weight')
    actions = ["export_as_csv"]
admin.site.register(Warehousestock, WarehousestockAdmin)
