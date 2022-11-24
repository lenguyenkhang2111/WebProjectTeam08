from django.contrib import admin

from purchase.models import Order, OrderDetail, Cart, CartItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartItem)
