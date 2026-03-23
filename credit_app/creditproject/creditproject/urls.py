"""
URL configuration for creditproject.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')),
    path('api/predictor/', include('predictor.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
