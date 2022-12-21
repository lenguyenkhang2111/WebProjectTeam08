from django.urls import path
from . import views
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment_history/', views.payment_history, name='payment_history'),
    path('purchased_courses/', views.purchased_courses, name='purchased_courses'),
]
