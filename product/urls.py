from django.urls import path
from . import views
urlpatterns = [
    path('', views.course, name='course'),
    path('detail', views.course_detail, name='course_detail')
]
