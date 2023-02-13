from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views

from .views import *

urlpatterns = [
    path('', users),
    path('is-admin/', is_admin),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', user, name='auth'),
    path('UpdateProfileView/', ProfileView, name='UpdateProfileView'),
    path('main-users/', main_users, name='auth'),
    path('login/', auth_views.obtain_auth_token)


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
