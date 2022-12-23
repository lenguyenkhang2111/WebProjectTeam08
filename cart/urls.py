from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<slug:course_slug>', views.add_cart, name='add_cart'),
    path('remove_cart_item/<int:cart_item_id>',
         views.remove_cart_item, name="remove_cart_item")
]
