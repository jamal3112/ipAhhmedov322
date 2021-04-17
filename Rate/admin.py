from django.contrib import admin

from .models import ServiceBid, TaximeterTarif, TaximeterValue

from import_export.admin import ImportExportModelAdmin

# admin.site.register(ServiceBid)
# admin.site.register(TaximeterTarif)
# admin.site.register(TaximeterValue)

@admin.register(ServiceBid)
class ServiceBidAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code_bid', 'driver', 'time_start', 'time_end')

@admin.register(TaximeterTarif)
class TaximeterTarifAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code_parameter', 'price', 'parameter_unit')

@admin.register(TaximeterValue)
class TaximeterValueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code_bid', 'code_parameter')

