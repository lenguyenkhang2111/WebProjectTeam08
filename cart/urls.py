from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('<slug:course_slug>/add_to_cart', views.add_cart, name='add_cart')
]
