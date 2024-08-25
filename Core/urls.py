from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from CollapseWeb import serializers, views

from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    
    path('api/', views.api, name='api'),
    path('api/', include(serializers.router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/analytics/start', views.analytics_start),
    path('api/analytics/client', views.analytics_client),
    
    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})
]

handler404 = 'CollapseWeb.views.handler404'
