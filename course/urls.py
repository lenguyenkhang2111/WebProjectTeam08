from django.urls import path
from . import views
urlpatterns = [
    path('', views.course, name='course'),
    path('<slug:course_slug>', views.course_detail, name='course_detail'),
    path('category/<slug:category_slug>',
         views.course, name='course_by_category'),
    path('search/', views.search, name='search'),
]
