from django.contrib import admin
from .models import Cart, CartItem
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(ImportExportModelAdmin):
    pass
