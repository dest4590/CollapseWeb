from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.models import User
from CollapseWeb import serializers
from . import settings

urlpatterns = [
    path('', include(serializers.router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)