from django.contrib import admin
from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'total',
                    'payment_status', 'placed_at')

    list_editable = ('payment_status',)

    @admin.display(description='Order')
    def pk(self, obj):
        return "Order " + str(obj.pk)


@admin.register(models.OrderDetail)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'course', 'price')

    @admin.display(description='Order Item')
    def pk(self, obj):
        return "Order Item " + str(obj.pk)
