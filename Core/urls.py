from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from CollapseWeb import serializers, views

from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    
    path('api/', views.index),
    path('api/', include(serializers.router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})
]
