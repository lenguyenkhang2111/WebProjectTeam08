from django.contrib import admin
from .models import Order, OrderDetail
from import_export.admin import ImportExportModelAdmin


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'user', 'total',
                    'payment_status', 'placed_at')

    list_editable = ('payment_status',)

    @admin.display(description='Order')
    def pk(self, obj):
        return "Order " + str(obj.pk)


@admin.register(OrderDetail)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'order', 'course', 'price')

    @admin.display(description='Order Item')
    def pk(self, obj):
        return "Order Item " + str(obj.pk)
