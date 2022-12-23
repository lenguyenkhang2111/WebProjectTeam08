from django.contrib import admin
from django.urls import path, include
from . import views
from account import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', user_views.profile, name='profile'),
    path('update/', user_views.update, name='update'),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
