from django.contrib import admin
from django.urls import path, include
from . import views
from account import views as user_views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', user_views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
