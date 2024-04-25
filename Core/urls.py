from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from .settings import MEDIA_ROOT, STATIC_ROOT
from CollapseWeb import views, serializers

urlpatterns = [
    path('', views.index),
    path('api/', views.api),
    path('api/', include(serializers.router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})
]